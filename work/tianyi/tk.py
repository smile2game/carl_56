T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    if m == 1:
        k = n // 2
        print(k)
        if k > 0:
            print(" ".join(str(i) for i in range(1, k + 1)))
        else:
            print()
    else:
        if n == 1:
            print(0)
            print()
        else:
            # Tk 拿 1..n-1 ，最大件 n 给弟弟
            print(n - 1)
            print(" ".join(str(i) for i in range(1, n)))
