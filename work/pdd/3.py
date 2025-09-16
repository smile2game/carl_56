import sys
from collections import defaultdict

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n = next(it)
A = [next(it) for _ in range(n)]

pref = 0
freq = defaultdict(int)
freq[0] = 1  # 空前缀
ans = 0

for x in A:
    pref += x - 1
    ans += freq[pref]
    freq[pref] += 1

print(ans)
