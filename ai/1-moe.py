import torch
import torch.nn as nn
import torch.nn.functional as F

class Expert(nn.Module):
    """单个 Expert：Linear -> GELU -> Linear"""
    def __init__(self, d_model, d_hidden):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_hidden)
        self.fc2 = nn.Linear(d_hidden, d_model)
    def forward(self, x):
        return self.fc2(F.gelu(self.fc1(x)))


class MoEFeedForward(nn.Module):
    """最简化版 MoE-FFN：Top-k 路由"""
    def __init__(self, d_model, d_hidden, num_experts, k=2):
        super().__init__()
        self.experts = nn.ModuleList([Expert(d_model, d_hidden) for _ in range(num_experts)])
        self.router = nn.Linear(d_model, num_experts)
        self.k = k

    def forward(self, x):
        """
        x: (B, S, D)
        return: (B, S, D)
        """
        B, S, D = x.shape
        N = B * S
        x_flat = x.view(N, D)

        # 路由 logits -> softmax
        logits = self.router(x_flat)          # (N, E)
        probs = F.softmax(logits, dim=-1)     # (N, E)

        # 取 top-k experts
        topk_prob, topk_idx = torch.topk(probs, self.k, dim=-1)  # (N, k), (N, k)

        # 初始化输出
        y = torch.zeros_like(x_flat)

        # 遍历每个 expert，处理属于它的 token
        for e, expert in enumerate(self.experts):
            # 找出哪些 token 的 topk 里有这个 expert
            mask = (topk_idx == e)  # (N, k) bool
            if mask.any():
                # token 索引
                token_idx, slot_idx = mask.nonzero(as_tuple=True)  # (M,), (M,)
                xin = x_flat[token_idx]       # 取出这些 token
                yout = expert(xin)            # 送进 expert
                gate = topk_prob[token_idx, slot_idx].unsqueeze(-1)  # 概率 (M,1)
                # 累加（因为可能有多个 expert 同时贡献给一个 token）
                y[token_idx] += gate * yout

        return y.view(B, S, D)


# ------------------ 使用示例 ------------------
if __name__ == "__main__":
    B, S, D = 2, 5, 16
    d_hidden = 64
    num_experts = 4

    moe_ffn = MoEFeedForward(D, d_hidden, num_experts, k=2)
    x = torch.randn(B, S, D)
    y = moe_ffn(x)
    print("input:", x.shape, "output:", y.shape)
