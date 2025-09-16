import sys
import heapq

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n = next(it); m = next(it); x = next(it)

a = [next(it) for _ in range(n)]
cnt = [0] * (n + 1)
for _ in range(m):
    d = next(it)
    cnt[d] += 1

heap = []  # 存 (cost, remain_capacity)
ans = 0

for day in range(1, n + 1):
    # 当天的 x 个名额入堆
    heapq.heappush(heap, (a[day - 1], x))

    need = cnt[day]  # 这一天之前必须发完的新增需求
    while need > 0:
        cost, cap = heapq.heappop(heap)
        take = cap if cap <= need else need
        ans += take * cost
        cap -= take
        need -= take
        if cap > 0:
            heapq.heappush(heap, (cost, cap))

print(ans)
