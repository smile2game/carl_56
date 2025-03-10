# 感悟：

工程和代码，debug只是 甜味小玩具，log和print才是真理



## 回溯基础

回溯 就是 暴力，回溯是递归的&#x20;

回溯都可以 抽象成为 树

### 解决的问题

* 组合： N个数字 找 k个数字，

  * 排列&#x20;

* 切割： 字符串按规则有几种切割

* 子集

* 棋盘&#x20;



模板代码

```python
def bt(参数)：
    if 终止:
        存放结果 
        return 
    for i in level:
        处理节点
        bt(路径，选择列表)
        回溯,撤销处理 
```





## 组合

### 77 组合&#x20;

类似深度优先搜索，但是有回退，接着深度，并非二叉树单纯的先后序，更像是 多叉树的 深度优先搜索&#x20;

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=N2M4ZjNiNDJjN2JlN2Y5M2Y2YWFkZWZkMGM5ZjFhMjZfYjlkZ3Z6a1FPdGVFOTc4UWtWNjdabkNEUGNMM1RSVDNfVG9rZW46Tmswb2JtMVNkb2ttUm94WGRPSWNrOWljbmw1XzE3NDE2MjU4NjQ6MTc0MTYyOTQ2NF9WNA)



```python
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def bt(self,n,k,startindex):
        """复杂度O(n * 2^n) """
        #终止条件 
        if len(self.path) == k:
            self.res.append(self.path[:])
            return
        #单层
        for i in range(startindex,n+1): #横向遍历 一遍
            self.path.append(i) #节点处理 
            self.bt(n,k,i + 1) #递归深入一层
            self.path.pop() #退回 
        

    def combine(self, n: int, k: int) -> List[List[int]]:
        """ startindex记录 递归搜索的起始位置"""
        self.bt(n,k,1)
        return self.res
```

#### 剪枝：

```python
#剪枝 剩余元素少于所需元素则不必遍历了 
n-i <= k - len(path)
>> 
i > n-(k - len(path)) + 1
#for的右边开 +1, >=应该逾越这个上线 +1 
for i in range(startindex,n-(k-len(self.path))+1+1): 
```



### 216 组合总和 3

这个太简单了&#x20;

```python
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def bt(self,n,k,startindex):
        #返回条件
        if len(self.path) == k:
            if sum(self.path) == n:self.res.append(self.path[:])
            return 

        #1-9遍历 
        for i in range(startindex,10):
            self.path.append(i)
            self.bt(n,k,i+1)
            self.path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.bt(n,k,1)
        return self.res
```

剪枝

```python
for i in range(startindex,10 - (k-len(self.path)) + 1):
```



### 17 电话号码的数字组合

小模版一套是真的简单&#x20;

自己都能摸出来了

```python
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.lmap = {
            "":"",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        } 

    def bt(self,digits,startindex):
        #返回 
        if len(self.path) == len(digits):
            self.res.append("".join(self.path[:]))
            return 
        #单层 
        # print(f"startindex is {startindex},digits[startindex] is {digits[startindex]}")
        letters = self.lmap[digits[startindex]]
        # print(f"letters is {letters}")
        for char in letters:
            self.path.append(char)
            self.bt(digits,startindex +1)
            self.path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        """不知道几个for"""
        if digits=="":return []
        self.bt(digits,0)
        return self.res
```



### 39 组合总和

注意 startindex,允许一直重复当前元素,但是还是往后走的,防止逆序重复

```python
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def bt(self,candidates,target,startindex):
        if sum(self.path) > target:
            return 

        if sum(self.path) == target:
            self.res.append(self.path[:])
            return 
        
        for i in range(startindex,len(candidates)):
            self.path.append(candidates[i])
            self.bt(candidates,target,i)
            self.path.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.bt(candidates,target,0)
        return self.res

```



### 40 组合总和2

```python
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def bt(self,candidates,target,startindex,used):
        if sum(self.path) > target:
            return 

        if sum(self.path) == target:
            self.res.append(self.path[:])
            return 
        
        for i in range(startindex,len(candidates)):
            if (candidates[i-1] == candidates[i] and used[i-1] == False): 
                print(f"同层")
                continue #当前这个,是上一次used False
            self.path.append(candidates[i])
            used[i] = True #这里标的是
            self.bt(candidates,target,i+1,used) #数字只能用一次,前进一步
            used[i] = False
            self.path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 
        时间复杂度 O(n 2^n) 
        树层去重的话，需要对数组排序
        树层重复,是使用过的不能再选取,不能有相同的组合
        树枝重复,同组合可以重复元素
        """
        candidates.sort()
        used = [0] * len(candidates)
        self.bt(candidates,target,0,used)
        return self.res 
```





## 分割:

### 分割模板：

```python
def is_or_not(s,start,end): #左闭右闭
    if xxx:
        return False
    return True

def bt(self,s,startindex,path,res):
    #终止条件
    if startindex >= len(s):
        if is_or_not(s,xxx,xxx): 
            res.append(path[:])
            
    #单层处理 
    for i in range(startindex,len(s):
        if is_or_not(s,startindex,i):
            path.append(s[startindex,i+1]) 
            self.bt(s,i + 1,,path,res) #更深一层，分割都是 i+1 
            path.pop()
            
def question(s):
    res = []
    self.bt(s,0,[],res)
    return res
```





* 我发现还是 把res和path传进去写起来 比较简单

### 131 分割回文串&#x20;

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=NThhMjgwYTI4MTA2NzM1OTBhMzU4NGJiMGVjYWZlYTNfNzcxSWFNWE84TzJIYW1wRDU2bFRlZWJsZk5qeTQ5ZGdfVG9rZW46Sk9vamJob0phb2I0bnh4NHlGT2M5cDlLbjAyXzE3NDE2MjU4NjQ6MTc0MTYyOTQ2NF9WNA)

* 字符串的截取也是 左开右闭的&#x20;

```python
class Solution:
    def isPalindrome(self,s,start,end):
        i,j = start,end
        while i< j:
            if s[i] != s[j]: return False
            i +=1
            j -=1 
        return True

    def bt(self,s,startindex,path,res):
        """ 切到 字符串最后是 终止条件 """
        if startindex >= len(s): 
            res.append(path[:])
            return 

        #单层处理 
        for i in range(startindex,len(s)): #(startindex,len(s))
            #子串是 [startindex,i]
            if self.isPalindrome(s,startindex,i): #是回文串 
                path.append(s[startindex:i+1])
                self.bt(s,i+1,path,res) #步进i+1
                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.bt(s,0,[],res)
        return res
```



### 93 复原ip地址

```python
```







## 子集







## 棋盘:

