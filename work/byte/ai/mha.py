import torch
torch.manual_seed(0)

def stable_softmax(x, dim=-1):
    x = x - x.max(dim=dim, keepdim=True).values
    ex = torch.exp(x)
    return ex / ex.sum(dim=dim, keepdim=True)

def mha(x, Wq, Wk, Wv, Wo, n_heads, causal=False, mask=None):
    """
    x: (B, T, D)
    Wq/Wk/Wv/Wo: (D, D)
    n_heads: 头数（D 必须能被 n_heads 整除）
    causal: 是否使用上三角因果掩码
    mask: 可选，形如 (B, 1, 1, T) 或可 broadcast 到 (B, 1, T, T)，True/1 表示可见
    返回: (B, T, D)
    """
    B, T, D = x.shape
    H = n_heads
    Dh = D // H

    # 线性映射得到 Q/K/V
    Q = x @ Wq   # (B, T, D)
    K = x @ Wk
    V = x @ Wv

    # 变换为 (B, H, T, Dh)
    Q = Q.view(B, T, H, Dh).transpose(1, 2)
    K = K.view(B, T, H, Dh).transpose(1, 2)
    V = V.view(B, T, H, Dh).transpose(1, 2)

    # 注意力得分 (B, H, T, T)
    scores = Q @ K.transpose(-2, -1) / (Dh ** 0.5)

    # 掩码：因果或外部 mask
    if causal:
        # 上三角置 -inf（不看未来）
        causal_mask = torch.triu(torch.ones(T, T, dtype=torch.bool, device=x.device), diagonal=1)
        scores = scores.masked_fill(causal_mask, float('-inf'))
    if mask is not None:
        # mask==0 的位置屏蔽
        scores = scores.masked_fill(~mask, float('-inf'))

    # 稳定 softmax
    attn = stable_softmax(scores, dim=-1)  # (B, H, T, T)

    # 加权求和得到各头输出，再拼回
    out = attn @ V                         # (B, H, T, Dh)
    out = out.transpose(1, 2).contiguous().view(B, T, D)  # (B, T, D)

    # 输出投影
    out = out @ Wo                         # (B, T, D)
    return out, attn

# ---------- 最小可运行示例 ----------
B, T, D, H = 2, 4, 8, 2
x  = torch.randn(B, T, D)
Wq = torch.randn(D, D) / (D ** 0.5)
Wk = torch.randn(D, D) / (D ** 0.5)
Wv = torch.randn(D, D) / (D ** 0.5)
Wo = torch.randn(D, D) / (D ** 0.5)

y, attn = mha(x, Wq, Wk, Wv, Wo, n_heads=H, causal=True)  # 改成 False 即非因果
print("y.shape:", y.shape)         # (B, T, D)
print("attn.shape:", attn.shape)   # (B, H, T, T)
