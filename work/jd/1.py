import torch 
from PIL import Image

print(f"torch version: {torch.__version__}")

MOD = 998244353

n_str = input().strip()       # 二进制表示，无前导0
L = len(n_str)
m = int(input().strip())

req_lsb = [-1] * L

for _ in range(m):
    p, o = map(int, input().split())
    if p >= L:
        if o == 1:
            print(0)
            raise SystemExit
    else:
        if req_lsb[p] == -1:
            req_lsb[p] = o
        elif req_lsb[p] != o:
            print(0)
            raise SystemExit

dp_tight = 1  # 初始前缀相等
dp_loose = 0


for pos in range(L):  # pos: [0..L-1]，高位->低位
    nbit = 1 if n_str[pos] == '1' else 0
    # 当前位对应低位下标
    p_lsb = L - 1 - pos
    req = req_lsb[p_lsb]  # -1/0/1

    allowed0 = (req == -1 or req == 0)
    allowed1 = (req == -1 or req == 1)
    k = (1 if allowed0 else 0) + (1 if allowed1 else 0)
    if k == 0:
        print(0)
        raise SystemExit

    new_tight = 0
    new_loose = 0

    new_loose = (new_loose + dp_loose * k) % MOD

    if nbit == 0:
        if allowed0:
            new_tight = (new_tight + dp_tight) % MOD
    else:  # nbit == 1
        if allowed0:
            new_loose = (new_loose + dp_tight) % MOD
        if allowed1:
            new_tight = (new_tight + dp_tight) % MOD

    dp_tight, dp_loose = new_tight % MOD, new_loose % MOD

ans = (dp_tight + dp_loose) % MOD
print(ans)


