a = [1,2,3,2,6]
n = len(a)

INF = -1e2
ans = 0
for d in range(2,5):
    dp0 = [INF] * (n+1) #no choose 
    dp1 = [INF] * (n+1) #process ith and chooses ith
    dp0[0] = 0 #no elem, is 0

    for i in range(1,len(a)+1): #开始下标错了 
        x = a[i-1]
        dp0[i] = max(dp0[i-1],dp1[i-1])
        
        if x%d == 0:
            dp1[i] = dp0[i-1] + 1
        else:
            dp1[i] = INF
    ans = max(ans,dp0[n],dp1[n])
    print(f"d is {d},ans is {ans},dp0 is {dp0},dp1 is {dp1}")
print(f"ans is {ans}")