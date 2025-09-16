# moe_ep_top2.py
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.distributed as dist


class Expert(nn.Module):
    def __init__(self, d_model, d_hidden):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_hidden)
        self.fc2 = nn.Linear(d_hidden, d_model)

    def forward(self, x):
        return self.fc2(F.gelu(self.fc1(x)))


class MoEEPTop2(nn.Module):
    """
    最简分布式 EP MoE（Top-2 路由），用 all_to_all_single 分发/回收。
    假设 num_experts % world_size == 0，每个 rank 拥有 num_experts/world_size 个 expert。
    """
    def __init__(self, d_model, d_hidden, num_experts, world_size, rank, device):
        super().__init__()
        assert num_experts % world_size == 0
        self.d_model = d_model
        self.num_experts = num_experts
        self.world_size = world_size
        self.rank = rank
        self.device = device

        self.local_experts = num_experts // world_size
        self.base_eid = rank * self.local_experts

        self.experts = nn.ModuleList(
            [Expert(d_model, d_hidden).to(device) for _ in range(self.local_experts)]
        )
        self.router = nn.Linear(d_model, num_experts).to(device)

    def forward(self, x):
        """
        x: (B, S, D)
        return: (B, S, D)
        """
        B, S, D = x.shape
        N = B * S
        x_flat = x.reshape(N, D)

        # 1) 路由 softmax -> Top-2
        logits = self.router(x_flat)                 # (N, E)
        probs = F.softmax(logits, dim=-1)            # (N, E)
        top2_prob, top2_idx = torch.topk(probs, 2, dim=-1)  # (N,2), (N,2)

        # 2) 为分发展开两份（每 token 复制两条）
        send_eid  = top2_idx.reshape(-1)                  # (2N,)
        send_gate = top2_prob.reshape(-1)                 # (2N,)
        send_orig = torch.arange(N, device=x.device).repeat_interleave(2)  # (2N,)

        # 3) 目标 rank（按 expert 全局 id 映射）
        dest_rank = send_eid // self.local_experts        # (2N,)

        # 4) 构造 per-rank 发送索引 & splits
        send_lists = [torch.nonzero(dest_rank == r, as_tuple=False).view(-1) for r in range(self.world_size)]
        send_splits = torch.tensor([len(ix) for ix in send_lists], device=x.device, dtype=torch.int64)
        total_send = int(send_splits.sum().item())

        if total_send > 0:
            order = torch.cat(send_lists, dim=0)
            s_x    = x_flat.index_select(0, send_orig.index_select(0, order))  # 按 orig 拿 token 向量
            s_eid  = send_eid.index_select(0, order)
            s_gate = send_gate.index_select(0, order)
            s_orig = send_orig.index_select(0, order)
        else:
            s_x    = torch.empty(0, D, device=x.device, dtype=x.dtype)
            s_eid  = torch.empty(0, device=x.device, dtype=torch.long)
            s_gate = torch.empty(0, device=x.device, dtype=x.dtype)
            s_orig = torch.empty(0, device=x.device, dtype=torch.long)

        # 5) 交换长度并分发（all_to_all_single）
        recv_splits = torch.empty_like(send_splits)
        dist.all_to_all_single(recv_splits, send_splits)

        recv_total = int(recv_splits.sum().item())
        r_x    = torch.empty(recv_total, D, device=x.device, dtype=x.dtype)
        r_eid  = torch.empty(recv_total, device=x.device, dtype=torch.long)
        r_gate = torch.empty(recv_total, device=x.device, dtype=x.dtype)
        r_orig = torch.empty(recv_total, device=x.device, dtype=torch.long)

        dist.all_to_all_single(r_x,    s_x,    out_split_sizes=recv_splits.tolist(), in_split_sizes=send_splits.tolist())
        dist.all_to_all_single(r_eid,  s_eid,  out_split_sizes=recv_splits.tolist(), in_split_sizes=send_splits.tolist())
        dist.all_to_all_single(r_gate, s_gate, out_split_sizes=recv_splits.tolist(), in_split_sizes=send_splits.tolist())
        dist.all_to_all_single(r_orig, s_orig, out_split_sizes=recv_splits.tolist(), in_split_sizes=send_splits.tolist())

        # 6) 本地 expert 计算（只处理自己负责的 experts）
        local_lid = r_eid - self.base_eid  # (recv_total,)
        y_local = torch.zeros_like(r_x)
        for lid in range(self.local_experts):
            sel = torch.nonzero(local_lid == lid, as_tuple=False).view(-1)
            if sel.numel() == 0:
                continue
            xin = r_x.index_select(0, sel)
            yout = self.experts[lid](xin)                  # (t_lid, D)
            gate = r_gate.index_select(0, sel).unsqueeze(-1)  # (t_lid, 1)
            y_local.index_copy_(0, sel, gate * yout)

        # 7) 回收（与分发相反方向）：把 y_local 与 r_orig 送回源 rank
        recv_back_splits = send_splits  # 源将接收与当初发送量相同的条目
        send_back_splits = recv_splits

        back_y    = torch.empty(int(recv_back_splits.sum().item()), D, device=x.device, dtype=x.dtype)
        back_orig = torch.empty(int(recv_back_splits.sum().item()), device=x.device, dtype=torch.long)

        dist.all_to_all_single(back_y,    y_local, out_split_sizes=recv_back_splits.tolist(), in_split_sizes=send_back_splits.tolist())
        dist.all_to_all_single(back_orig, r_orig,  out_split_sizes=recv_back_splits.tolist(), in_split_sizes=send_back_splits.tolist())

        # 8) 在源 rank 聚合两份贡献：按 orig 累加
        y_flat = torch.zeros(N, D, device=x.device, dtype=x.dtype)
        if back_orig.numel() > 0:
            y_flat.index_add_(0, back_orig, back_y)  # 同一 token 两条贡献求和

        return y_flat.view(B, S, D)


def setup_dist():
    rank = int(os.environ["RANK"])
    world_size = int(os.environ["WORLD_SIZE"])
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    device = torch.device(f"cuda:{local_rank}" if torch.cuda.is_available() else "cpu")
    torch.cuda.set_device(device) if device.type == "cuda" else None
    backend = "nccl" if device.type == "cuda" else "gloo"
    dist.init_process_group(backend=backend, init_method="env://")
    return rank, world_size, device


def main():
    rank, world_size, device = setup_dist()

    # 超参数（可随意改）
    B, S, D = 2, 8, 64
    d_hidden = 256
    num_experts = 8  # 例如 world_size=4 -> 每卡 2 个 expert

    moe = MoEEPTop2(D, d_hidden, num_experts, world_size, rank, device)

    x = torch.randn(B, S, D, device=device)
    y = moe(x)

    if rank == 0:
        print("Output shape:", tuple(y.shape))

    dist.barrier()
    dist.destroy_process_group()


if __name__ == "__main__":
    main()
