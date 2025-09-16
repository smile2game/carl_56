# file.py
# LoRA Self-Attention (Q only) in float64, read from STDIN
import sys
import numpy as np
import math

def read_tokens():
    data = sys.stdin.read()
    return data.strip().split()

def main():
    toks = read_tokens()
    it = iter(toks)

    # b: number of tokens (sequence length), d: feature dim, r: LoRA rank
    b = int(next(it)); d = int(next(it)); r = int(next(it))

    # X: (b, d)
    X = np.array([float(next(it)) for _ in range(b * d)], dtype=np.float64).reshape(b, d)

    # Wq, Wk, Wv: each (d, d)
    def read_mat_dd():
        return np.array([float(next(it)) for _ in range(d * d)], dtype=np.float64).reshape(d, d)

    Wq = read_mat_dd()
    Wk = read_mat_dd()
    Wv = read_mat_dd()

    # A: (r, d), B: (d, r) when r > 0; else treat as zero contribution
    if r > 0:
        A = np.array([float(next(it)) for _ in range(r * d)], dtype=np.float64).reshape(r, d)
        B = np.array([float(next(it)) for _ in range(d * r)], dtype=np.float64).reshape(d, r)
        BA = B @ A  # (d, d)
    else:
        BA = np.zeros((d, d), dtype=np.float64)

    # Column-vector convention via right-multiply with transposed weights
    Wq_eff_T = (Wq + BA).T
    K_T = Wk.T
    V_T = Wv.T

    Q = X @ Wq_eff_T          # (b, d)
    K = X @ K_T               # (b, d)
    V = X @ V_T               # (b, d)

    # Scaled dot-product attention: softmax over rows
    scale = math.sqrt(d)
    logits = (Q @ K.T) / scale         # (b, b)
    logits -= logits.max(axis=1, keepdims=True)
    np.exp(logits, out=logits)
    logits /= logits.sum(axis=1, keepdims=True)

    Y = logits @ V  # (b, d)

    # Print flattened row-major with 4 decimals
    out = Y.reshape(-1)
    print(" ".join(f"{v:.4f}" for v in out))

if __name__ == "__main__":
    main()
