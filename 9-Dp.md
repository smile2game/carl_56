# 感悟

1. 思路想明白了再写，真的很简单



# 基础

拆解舞步：&#x20;

1. 确定 dp数组 与 下标 的含义

2. 写递推公式

3. dp数组 初始化  (递推公式 决定 初始化)

4. 确定遍历顺序

5. 举例模拟  dp数组 &#x20;



debug小技巧： 反问自己&#x20;

* 模拟

* 打印dp数组 和 模拟对照&#x20;

  * 如果和模拟一样，那就是 递推公式，初始化，遍历顺序有问题















## 基本 思路&#x20;

### 509 斐波那契数

```python
class Solution:
    def fib(self, n: int) -> int:
        """ 
        dp[i]: i表示第几个数字,val代表值,
        dp[i] = dp[i-1] + dp[i-2]
        dp[0] = 0,dp[1] = 1, 尺寸是 n+1,求的是 F(n)注意F(0)背刺
        0>>N

        """
        if n == 0:return 0
        if n==1: return 1
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(f"dp is {dp}")
        return dp[n]
```





### 70 爬楼梯

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        """ 
        dp[i] : i is 第i阶楼梯, val is 方法数量
        dp[i] = dp[i-1] + dp[i-2]
        dp[0]= 0,dp[1] = 1,尺寸是 n+1

        """
        if n == 0:return 0
        if n==1: return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(f"dp is {dp}")
        return dp[n]
```



### 746 使用最小花费爬楼梯

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """ 
        define:
        dp[i], i is ith level, val is cost of ith level
        dp[i] = min(cost[i-1] + dp[i-1],cost[i-2] + dp[i-2])
        init:
        dp[0] = 0,dp[1] = 0, size is (n+1)
        order:
        0 >> N
        """
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(dp)):
            dp[i] = min(cost[i-1] + dp[i-1],cost[i-2] + dp[i-2])
            # print(f"dp is {dp}")
        return dp[-1]
```



### 62 不同路径

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        define:
        dp[i][j], (i,j) is position,val is num of methods
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        init:
        dp[0][i] = 1
        dp[j][0] = 1
        sort:
        >> 
        下
        res:
        return dp[m-1][n-1]
        """
        dp = [[0]*(n) for _ in range(m)] 
        #init 
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[m-1][n-1]
```

### 63 带上障碍物:

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*(n) for _ in range(m)] 
        #init 
        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[m-1][n-1]
```





### 343 整数拆分

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        dp[i] : i的拆分
        dp[i] = max{dp[i],j*(i-j),j*dp[i-j]}
        """
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3,n+1): #
            for j in range(1,i):
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
                print(f"i is {i},j is {j},dp[{i}] is {dp[i]}")
        return dp[n]

        
```





# 01背包

## 理论基础:

* w\[i] & v\[i]

* 只能选一次&#x20;

```python
""" 
define
dp[i][j],i is ith物品, j is 背包容量, val is val (给的也是 物品数量和背包容量,一般给的都是下标)
dp[]
"""
```





### Carl 46 携带研究材料&#x20;

* 注意，物品下标从1开始，但是容量从0开始

```python
m,n = map(int,input().split())

weight = list(map(int,input().split()))
val = list(map(int,input().split()))

# print(f"weight is {weight},val is {val}")

"""
define 
dp[i][j],i is ith物品, j is 背包容量, val is max val (给的也是 物品数量和背包容量,一般给的都是下标)
dp[i][j] = max(val[i] + dp[i-1][j-weight[j]] , dp[i-1][j]) #拿 - 不拿 

init:
size = mx(n+1), 因为容量应该多出来一个kong

dp[i][0] = 0
if j>= weight[0]:
    dp[0][j] = val[0]

sort: 为什么?
>>
下

"""
dp = [[0]*(n+1) for _ in range(m)]
for j in range(n+1):
    if j >= weight[0]:
        dp[0][j] = val[0]

for i in range(1,m):
    for j in range(1,n+1):
        if j< weight[i]: dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], val[i] + dp[i-1][j-weight[i]])
        # print(f"dp is {dp}")
        
print(dp[m-1][n])
```



滚动数组：

```python
```







