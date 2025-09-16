T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    c = arr[0] ^ 1  # 假设常量 c = a1 ^ 1
    ok = True
    for i in range(1, n):  # 下标 i 从 1 开始（对应题目 i=2..n）
        if (arr[i] ^ (i + 1)) != c:
            ok = False
            break
    print("Yes" if ok else "No")