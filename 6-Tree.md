# 复盘：

## 3.6 last day

### 递归遍历&#x20;

```python
def __init__(self):
    self.res = []
def pre_dfs(self,root):
    if root==None:return None
    
    self.res.append(root.val)
    self.dfs(root.left)
    self.dfs(root.right)
    return root 
```

* 翻转，非中序，交换左右子树

  ```python
  root.left,root.right = root.right,root.left 
  dfs(root.left)
  dfs(root.right)
  #这俩也能调转，贼好玩 
  ```

* 对称检查

```python
def compare(self,left,right): #想明白，需要返回值来记录对称状态 
    #终止条件 
    if (left == None and right == None): return True #即使 左右儿子 值相等，未必对称，还需要递归检查 
    elif (left == None and right != None) or (left!=None and  right == None) or (left.val != right.val): return False
    #递归
    equal_out = self.compare(left.left,right.right)
    equal_in = self.compare(left.right,right.left)
    return equal_in and equal_out    
```

* 最大深度:

```python
```

* 最小深度:

* 求节点数量

```python
def countNodes(self, root: Optional[TreeNode]) -> int:
    if root==None: return 0
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

&#x20;&#x20;



### 层序遍历&#x20;

```python
def level_bds(self,root):
    if root == None: return []
    que = deque([root]) #不放进来你搞个狗子
    res = []
    while que:
        level = []
        for _ in range(len(que)):
            cur = que.popleft()
            level.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        res.append(level)
    return res
```

* 层平均值，最大值，最右边值

* 右视图，填充右侧节点

* 最大深度/最小深度







## 小技巧

* 树的debug,就是在 迭代刚进入时候 `print(f"cur.val is {cur.val}")`,如果溢出就在 终止条件加 else

* 能提前开数组空间保存的思路一定要采用，空间不仅能换时间复杂度还能换思路的简单

* 路径题目适合记录返回值，前序遍历，并记录cnt。&#x20;

  * 路经综合2，要记录全部路径也要return，但是就不需要返回bool值判断了

* 递归的返回是 函数这次调用返回,不是全局的返回&#x20;

* 带上返回就是 回溯，返回值回溯传递

* 只要没有 中节点的处理，就不用在乎 遍历顺序了&#x20;

# 感悟

* 递归三要素,树 太推荐跟着 代码随想录了,上一个这么爽的还是 动态规划,搞明白定义真的很重要

* 树还是需要二刷的，感觉有些缺少总结性，或者我等会总结一下

* 学算法题，学到后面，其实实现自己的思路都已经不难了，解题的难点就在于思路(降低复杂度)和复杂度分析

  * 而如果你连实现的能力都没有，那就属于还没有入门，AI也是如此







# 基本数据结构

## 基础知识

python的类方法里还能 再定义功能函数：

```python
class A(self):
    def B(x):
        def C(x)：
            proc(x)
        res = C(x)
        return res
```



* 平衡二叉搜索树，左右差 <= 1

C++中map、set、multimap，multiset的底层实现都是平衡二叉搜索树，python的dict和set用的是哈希表。



* 存储方式

链式：指针&#x20;

顺序：数组



## 基本定义：

```python
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right 
```

* 深度优先遍历

  * 前序遍历（递归法，迭代法）

  * 中序遍历（递归法，迭代法）

  * 后序遍历（递归法，迭代法）

* 广度优先遍历

  * 层次遍历（迭代法）







# 层序遍历：

## 102 二叉树的层序遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root]) #双端
        # print(que)
        res = []
        while que:
            level = []
            for _ in range(len(que)): #访问当前层所有Node，放入下层所有Node
                cur = que.popleft()
                print(f"{_}层, cur.val is {cur.val}")
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(level)
        return res
```

* 102 二叉树的层序遍历

* 199 二叉树右视图&#x20;

level\[-1]

* 637 层平均值&#x20;

* 429 N叉树

```python

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root: return res
        que = deque([root]) 
        while que:
            level = [] 
            for _ in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                for k in range(len(cur.children)):
                    if cur.children[k]:
                        que.append(cur.children[k])
                # if cur.left:
                #     que.append(cur.left)
                # if cur.right:
                #     que.append(cur.right)
            res.append(level)
        return res
```

* 116 填充节点&#x20;

* 117 填充节点2 根本没变

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            # print("root 是空的")
            return root #这个还挺骚的
            
        que = deque([root]) #双端

        while que:
            level = []
            for _ in range(len(que)): #访问当前层所有Node，放入下层所有Node
                cur = que.popleft()
                # print(f"{_}层, cur.val is {cur.val}")
                level.append(cur)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None
        return root
```

* 104 最大深度

* 111 最小深度

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root]) #双端
        # print(que)
        res = 0
        while que:
            for _ in range(len(que)): #访问当前层所有Node，放入下层所有Node
                cur = que.popleft()
                # print(f"{_}层, cur.val is {cur.val}")
                # level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res+=1
        return res
```





# 递归遍历：

前求深度(node,height)，

后求高度(node)， 返回值累加问题

中间求路径(cur,path,res)



递归三要素：

1. 参数和返回值

2. 终止条件

3. 单层递归的逻辑

   1. 例如调整前中后次序



前中后指的是中节点出现的次序

* 144 前序遍历：中左右

* 94 中序遍历：左中右

* 145 后序遍历：左右中

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #全局的res
        #单层逻辑
        def dfs(node):
            if node == None: return #终止条件
            # print(f"res.append({node.val})")
            # print(f"res is {res}")
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
        

```



## 迭代遍历(暂时跳)









## 226 反转二叉树

反转别用中序

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """max howell的伤心地
        中序会翻两次
        迭代: 单层处理
        终止条件
        入口出口：参数和返回值
        """
        def dfs(root):
            if root is None: return 
            #先序
            # print(f"root.val is {root.val}")
            dfs(root.left)
            root.left,root.right = root.right,root.left
            dfs(root.right)
        dfs(root)
        print(root)
        return root
            

```



## 101 对称二叉树

* 回溯，后序遍历， 外层内层

* 递归： 参数和返回值 >> 终止条件 >> 单层处理&#x20;

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
          1         
        2   2
       3 4 4  4
       i      j
        """
        def compare(left,right):
            #终止条件 
            if (left==None and right==None): 
                # print(f"left.val is {left.val},right.val is {right.val}")
                return True
            elif  (left == None and right!=None) or (left != None and right == None ) or (left.val != right.val): return False

            #单步处理,处理下一层的外侧和内侧
            outside = compare(left.left,right.right)
            inside = compare(left.right,right.left)
            return outside and inside

        # if not root: return None
        return compare(root.left,root.right)
```

# 深度与高度

## 104 二叉树的最大深度

前深 后高&#x20;



根节点的高度 == 二叉树的深度&#x20;

```python
"""
  1         |根节点的高度 = 3
2   2       |
           ---
3 4 4  4    |叶节点的深度 = 3
i      j
"""

#后序，简单的求根据节点的高度
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """后序求 高度， 前序求深度"""
        def getDepth(node):
            if node == None: return 0
            l_d = getDepth(node.left)
            r_d = getDepth(node.right)
            depth = 1 + max(l_d, r_d) #求解或处理
            return depth
        res = getDepth(root)
        return res
        
```

非常重要的 nonlocal，python的全局变量&#x20;

```python
#前序，求叶子节点的深度
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """后序求 高度， 前序求深度"""
        res = 0
        def getDepth(node,depth):
            #终止条件
            nonlocal res
            if node == None: return 
            #单层处理 
            res = max(depth,res) #在这记录是因为，需要用到的返回值
            if node.left: getDepth(node.left,depth+1)
            if node.right:getDepth(node.right,depth+1)
            return 
            
        getDepth(root,1)
        return res


class Solution:
    def __init__(self):
        self.res = float('inf')

    def getDepth(self,node,depth):
        if node == None: return 
        if node.left == None and node.right == None: self.res = min(self.res,depth)

        if node.left: self.getDepth(node.left,depth + 1)
        if node.right: self.getDepth(node.right,depth+1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """后序好实现"""
        if root is None: return 0
        self.getDepth(root,1)
        return self.res
```



## 111 二叉树最小深度&#x20;

两个都空就是最小深度&#x20;



后序法：

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """后序好实现"""
        def getHeight(node):
            #终止条件 
            if node == None: return 0
            #单层
            l_d = getHeight(node.left)
            r_d = getHeight(node.right)
            #由于min导致的
            if node.left == None and node.right != None:
                return r_d + 1
            if node.left != None and node.right == None:
                return l_d + 1
            Height = 1 + min(l_d,r_d)
            print(f"node.val is {node.val},minHeight is {Height}")
            return Height
        return getHeight(root)
```

前序法反而更直观呢：

* 前序求深度

```python
class Solution:
    def __init__(self):
        self.res = float('inf')

    def getDepth(self,node,depth):
        if node == None: return 
        if node.left == None and node.right == None: self.res = min(self.res,depth)

        if node.left: self.getDepth(node.left,depth + 1)
        if node.right: self.getDepth(node.right,depth+1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """后序好实现"""
        if root is None: return 0
        self.getDepth(root,1)
        return self.res
```



## 222 完全二叉树跳了&#x20;

层序遍历直接做&#x20;



## 110 平衡二叉树&#x20;

后序遍历求高度，太简单了

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """ 高度必须 从下往上查 """
        def getHeight(node):
            if node == None: return 0

            l_d = getHeight(node.left)
            r_d = getHeight(node.right)
            if l_d == -1 or r_d == -1:
                return -1 
            else:
                if abs(l_d - r_d) > 1:
                    return -1 
                else:
                    Height = 1 + max(l_d,r_d)
            return Height  
        return getHeight(root) != -1
```

## 404 左叶子之和：

感觉左叶子之和这道题好像讲的和写的都有点复杂了，其实终止条件只需要一条

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """ 后序 """
        #终止条件
        if root == None: return 0 #叶子之后，返回0
        #单层递归
        l_sum = self.sumOfLeftLeaves(root.left) #左
        if root.left and not root.left.left and not root.left.right: l_sum = root.left.val
        r_sum = self.sumOfLeftLeaves(root.right) #右，不可能是左叶子，所以不需要上面if
        m_sum = l_sum + r_sum #后后序
        return m_sum
```



## 513 找树左下角的值

```python
class Solution:
    def __init__(self):
        self.maxDepth = 0
        self.res = 0
        
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """ 先序 求 深度 
        先序:传值，不返回
        """
        def pre_dfs(node,depth): #depth好像属性一样
            #终止 
            if node == None: return 
            if node.left == None and node.right == None: #本来就是第一个遇到的叶子节点一定是最左边的吧，遍历到的就是
                if depth > self.maxDepth: 
                    self.maxDepth = depth
                    self.res = node.val
                return 
            pre_dfs(node.left,depth+1)
            pre_dfs(node.right,depth+1)
        pre_dfs(root,1)
        print(f"self.maxDepth is {self.maxDepth}")
        return self.res
```



# 回溯找路径

## 257 二叉树的所有路径

* 开始和 回溯，其实挺简单的，就是递归完之后，pop代表回溯了嘛

```python
class Solution:
    def traversal(self,cur,path,res):
        path.append(cur.val) #中间
        if not cur.left and not cur.right: #左右都没有，就是叶子节点
            sPath = '->'.join(map(str,path)) #全部拼起来
            res.append(sPath)
            return  
        if cur.left:
            self.traversal(cur.left,path,res)
            path.pop() #走过了，退回来
        if cur.right:
            self.traversal(cur.right,path,res)
            path.pop() #走过了，退回来 

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """ 路径适合前序遍历 """
        res = []
        path = []
        if not root: return res
        #遍历一下
        self.traversal(root,path,res)
        return res
```



# 找路径

路径题目适合记录返回值，前序遍历，并记录cnt

## 513 路经总和&#x20;

递归函数的返回,是是否满足路径

```python
class Solution:
    def traversal(self, cur: TreeNode, cnt: int) -> bool:
        print(f"cur.val is {cur.val}")  #非常良好的树debug

        if not cur.left and not cur.right and cnt == 0: # mid,遇到叶子节点，并且计数为0
            if cnt == 0:
                print(f"中子树的满足,cnt is {cnt}") 
                return True
            else:
                print(f"叶子节点,且不是满足的路径") 
                return False
        
        if cur.left: #left
            if self.traversal(cur.left,cnt-cur.left.val):
                print(f"左子树的满足,cnt is {cnt}") 
                return True
            
        if cur.right: #右
            if self.traversal(cur.right,cnt - cur.right.val):
                print(f"右子树的满足,cnt is {cnt}")
                return True
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root, targetSum - root.val)      
```



## 113 路经总和2&#x20;

```python
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def traversal(self,cur,cnt):
        # print(f"cur.val is {cur.val},cnt is {cnt},self.path is {self.path},self.res is {self.res}")
        if not cur.left and not cur.right: #中直接不做处理,在调用前把root放入,然后left和right时候再 处理path
            # print(f"到达叶子节点: {cur.val},cnt==0 is {cnt==0}")
            if cnt==0:
                # print(f"满足,self.path is {self.path}")
                self.res.append(self.path[:]) #列表里放列表要这样放
            return 

        if cur.left:
            self.path.append(cur.left.val)
            self.traversal(cur.left, cnt - cur.left.val)
            self.path.pop()
        if cur.right:
            self.path.append(cur.right.val)
            self.traversal(cur.right, cnt - cur.right.val)
            self.path.pop()
        return 
 

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """ 找到所有路径,所以不要返回值来判断 True or False """
        if root is None:return []
        self.path.append(root.val)
        self.traversal(root,targetSum-root.val)
        return self.res
```



# 构建树&#x20;

## 106 中序 后序恢复一个二叉树

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """ 
        note: 左闭右开，注意 边界值 
        逻辑：
        1. 后序数组最后一个点 是 中序数组 左右子树 切割点,切割
        2. 后序数组左右子树 和 中序数组 尺寸一致,切割
        3. 递归左右子树 
        """
        if not inorder:
            return None
        #当前点
        cur_val = postorder[-1]
        cur = TreeNode(cur_val)

        #切割中序 
        # print(f"cur_val is {cur_val},inorder is {inorder}")
        inorder_split = inorder.index(cur_val)
        inorder_l = inorder[:inorder_split] #左闭右开
        inorder_r = inorder[inorder_split+1:] #左闭右开
        #切割后序
        postorder_l = postorder[:len(inorder_l)]
        postorder_r = postorder[len(inorder_l):-1]

        #递归左右 
        cur.left  = self.buildTree(inorder_l,postorder_l)
        cur.right = self.buildTree(inorder_r,postorder_r)
        return cur
```

## 654 最大二叉树&#x20;

*

```python
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """ 构建树 用先序遍历 """
        #终止条件
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        maxValue = max(nums)
        cur = TreeNode(maxValue)

        #切割 
        sep_idx = nums.index(maxValue)
        nums_l = nums[:sep_idx]
        nums_r = nums[sep_idx+1:]

        #左右递归
        cur.left = self.constructMaximumBinaryTree(nums_l)
        cur.right = self.constructMaximumBinaryTree(nums_r)
        return cur
```



## 合并二叉树

* 什么顺序 都一样

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 后序-利用Tree1 """
        #中 + 终止条件- 叶子节点提前离开，就是终止条件
        if root1 is None: return root2
        if root2 is None: return root1
        print(f"root1.val is {root1.val},root2.val is {root2.val}")

        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        root1.val = root1.val + root2.val
        return root1
```



# 二叉搜索树：(BST)

* 左子树小于根，右子树大于根，递归满足



## 700 BST搜索&#x20;

```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ 可以有顺序的去搜索
        BST 是需要返回值存储答案的 
        """ 
        # 终止条件
        if root == None: return None
        # 先序
        if root.val == val: return root  
        if val < root.val:  return  self.searchBST(root.left,val)
        if val > root.val: return  self.searchBST(root.right,val)
```



## 98 验证二叉搜索树&#x20;

中序 用数组存储就可以了

```python
class Solution:
    def __init__(self):
        self.nums = []
    def traversal(self,root):
        if root == None: return 
        self.traversal(root.left)
        self.nums.append(root.val)
        self.traversal(root.right)
        return 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ 中序遍历验证单增 """
        self.traversal(root)
        for i in range(1,len(self.nums)):
            if self.nums[i-1] >= self.nums[i]:
                return False
        return True
```



## 501 二叉搜索树的众数

* 利用二叉搜索树的性质来写，不太明智，建议直接用map

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0
        self.maxCnt = 0
        self.pre = None
        self.res = []

    def in_dfs(self,root):
        #终止
        if root == None: return 
        
        self.in_dfs(root.left)
        #中
        if self.pre == None:
            self.cnt = 1
        elif self.pre.val == root.val:
            self.cnt += 1
        else:
            self.cnt =1
        self.pre = root #前进 pre

        if self.cnt == self.maxCnt: self.res.append(root.val)
        elif self.cnt > self.maxCnt: 
            self.maxCnt = self.cnt
            self.res = [root.val]
        self.in_dfs(root.right)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.in_dfs(root)
        return self.res
```

* map大法好

唯一真神

```python
class Solution:
    def __init__(self):
        self.freq_map = defaultdict(int) #默认值为0

    def in_dfs(self,root):
        #终止
        if root == None: return 
        self.in_dfs(root.left)
        self.freq_map[root.val] += 1 
        self.in_dfs(root.right)
        
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.in_dfs(root)
        maxCnt = max(self.freq_map.values())
        for k in self.freq_map.keys():
            if self.freq_map[k] == maxCnt:
                res.append(k) 
        return res
```





## 236 二叉树的最近公共祖先 （查找）

非常 牛逼的一道 回溯题目&#x20;

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=YWY5ZWNmMWMyMjE0M2FlMGFlNTUxMDZiNWJlNmJjYTBfVWEydUlMT1h2MUE4VEk0TE9KeWc5UU44MVY2QTYzZU5fVG9rZW46TGQzWmJEdGI3bzRTd0h4UHF2QWNHQUQ2bnFkXzE3NDEyNzg4OTU6MTc0MTI4MjQ5NV9WNA)



```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
        单边 if(dfs(root.left)): return 
        全树 left = dfs(root.left) 关键在于不返回
        """
        #终止条件 
        if root == q or root == p or root == None: return root #找到了就返回他

        #单层处理 
        #全树遍历,且后序遍历
        left = self.lowestCommonAncestor(root.left,p,q) #左侧返回节点 
        right =  self.lowestCommonAncestor(root.right,p,q)

        if left is not None and right is not None: return root #左也对，右也对，那就是他了

        if left is not None and right is None: return left #左对，右不对，继承左边返回值 
        elif left is None and right is not  None: return right  
        else: return None #两边都没有，继续往上传递None
```





## 235 二叉搜索树的最近公共祖先

* 只要没有 中节点的处理，就不用在乎 遍历顺序了&#x20;

*

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
        dfs最先 in [p,q]的就是最近公共祖先， 因为再向下走就会错过 左边或者右边  
        再探再报!
        """
        if root is None: return root

        if p.val < root.val and q.val < root.val: 
            l = self.lowestCommonAncestor(root.left,p,q)
            if l != None: return l
        if p.val > root.val and q.val > root.val: 
            r = self.lowestCommonAncestor(root.right,p,q)
            if r!=None:return r
        return root
```



## 插入&#x20;

```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #
        if root == None: 
            return TreeNode(val) #即使是一个空树也要对其进行构造
        
        #二叉搜索树的遍历
        if root.val > val: 
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left,val)
        if root.val < val: 
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right,val)
        return root
```



## 删除

```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """ 
        先序遍历

        通用 删除方法: 
        左子树 迁移到 右子树最右边节点 
        如果 右子树是空的就直接 挂在这里, (返回值就是接的地方) 为什么交换替代悬挂???
        """
        if root == None: return root 
        print(f"root.val is {root.val}")
        #中间 处理 
        if root.val == key: 
            if root.right == None: return root.left #
            #寻找右子树的最左边
            cur = root.right #右子树 
            while cur.left: cur = cur.left #最左节点
            cur.val,root.val =  root.val,cur.val

        root.left =  self.deleteNode(root.left,key) #构造左子树,回溯
        root.right =  self.deleteNode(root.right,key) #构造右子树
        return root 
```

## 修剪

```python
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """ 暴力 当然不行了 """
        if root == None: return None
        #单层处理 
        if root.val < low:  return self.trimBST(root.right,low,high) #太小，就返回右子树，就把自己跳过了
        if root.val > high: return self.trimBST(root.left,low,high)
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root  
```

## 转换

### 有序数组转化为 二叉搜索树&#x20;

```python
class Solution:
    """构建时候不用传入root,只需要返回root """
    def dfs(self,nums,left,right):
        if left>right: return
        mid = left + (right - left)//2 #加法小妙招 = (left+root)//2,同时防止溢出
        #先序
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums,left,mid-1) 
        root.right = self.dfs(nums,mid+1,right)
        return root 

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums,0,len(nums)-1)
```



### 二叉搜索树转化为 累加树

```python
class Solution:        
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 二叉搜素树 的 从右往左累加 """  
        if root == None: return 
        #右
        self.convertBST(root.right) 
        #中 
        root.val += self.sum
        self.sum = root.val 
        #左
        self.convertBST(root.left)
        return root 
```
