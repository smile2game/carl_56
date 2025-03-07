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

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=ODliZmIxNGM2NDcwNWJhZThhZThjNmJjOTdjZjNiNmJfZkNRN3JPeXBPWWd1VzllNlVhSG1kWkhMb1NmZW9UVElfVG9rZW46Tmswb2JtMVNkb2ttUm94WGRPSWNrOWljbmw1XzE3NDEzMzQ2MDA6MTc0MTMzODIwMF9WNA)



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

```python
```
