# -*- coding: utf-8 -*-
import sys
import numpy as np

def main():
    data = sys.stdin.read().strip().split()
    # 读第一行：b d r
    b, d, r = map(int, data[:3])
    nums = list(map(float, data[3:]))

    need = {
        "x": b * d,
        "Wq": d * d,
        "Wk": d * d,
        "Wv": d * d,
        "Wu": d * d,
    }
    if r > 0:
        need["A"] = r * d
        need["B"] = d * r

    # 按顺序切片
    idx = 0
    def take(n):
        nonlocal idx
        arr = nums[idx: idx + n]
        idx += n
        return np.array(arr, dtype=np.float64)

    X  = take(need["x"]).reshape(b, d)
    Wq = take(need["Wq"]).reshape(d, d)
    Wk = take(need["Wk"]).reshape(d, d)
    Wv = take(need["Wv"]).reshape(d, d)
    Wu = take(need["Wu"]).reshape(d, d)

    if r > 0:
        A = take(need["A"]).reshape(r, d)   # r x d
        B = take(need["B"]).reshape(d, r)   # d x r
        Wq_eff = Wq + B @ A                 # d x d
    else:
        Wq_eff = Wq

    # Q, K, V
    Q = X @ Wq_eff          # b x d
    K = X @ Wk              # b x d
    V = X @ Wv              # b x d

    # Attention: softmax((Q K^T) / sqrt(d))
    scale = 1.0 / np.sqrt(float(d))
    logits = (Q @ K.T) * scale            # b x b
    logits = logits - logits.max(axis=1, keepdims=True)  # 数值稳定
    attn = np.exp(logits)
    attn = attn / attn.sum(axis=1, keepdims=True)        # b x b

    # 输出投影
    Y = (attn @ V) @ Wu                    # b x d

    # 展平输出，四位小数
    out = Y.reshape(-1)
    print(" ".join(f"{x:.4f}" for x in out))

if __name__ == "__main__":
    main()
