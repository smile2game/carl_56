from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

n, q = map(int, input().split())
a = list(map(int, input().split()))

# 降序排序 + 前缀和
a.sort(reverse=True)
ps = [0] * (n + 1)
for i in range(n):
    ps[i + 1] = ps[i] + a[i]
total = ps[n]

for _ in range(q):
    x, y = map(int, input().split())
    L = lcm(x, y)
    k_plus = n // x - n // L
    k_minus = n // y - n // L

    sum_plus = ps[k_plus]
    if k_minus == 0:
        sum_minus = 0
    else:
        sum_minus = total - ps[n - k_minus]

    print(sum_plus - sum_minus)
