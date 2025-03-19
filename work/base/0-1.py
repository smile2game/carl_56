m,n = 6,1
weight = [2,2,3,1,5,2]
val = [2,3,1,5,4,3]


dp = [[0]*(n+1) for _ in range(m)]
for j in range(n+1):
    if j >= weight[0]:
        dp[0][j] = val[0]

for i in range(1,m):
    for j in range(0,n+1):
        if j< weight[i]: dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], val[i] + dp[i-1][j-weight[i]])
        print(f"dp is {dp}")
        
print(dp[m-1][n])

