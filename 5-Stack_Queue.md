Python 标准库中没有专门定义栈（stack）这个数据结构

# 题目总结

* 栈实现队列，两个栈互相倒一下就可以

* 队列实现栈也是互相倒一下，用deque()

* 有效括号，逆波兰表达式，删除重复项，都是用栈对对碰

* 滑动窗口维护单调队列

* 前K个高频元素是维护 优先队列(数值越大越先出去) (背后实现是 小顶堆)

# 感悟

* 如果我们总想着最少的代码量的话，那作为程序员就没有意义了，应当是先用代码描绘出正确的逻辑，在考虑精简代码逻辑，而不是一开始就不想动手写代码

* 遇到问题时侯，应当脑子中首先出现的是暴力的解法或者常规的解法，然后才开始用数据结构来进行优化，关键点在于有暴力思路>>优化思路

* 编程的核心逻辑是 数据形态 + 可用容器和方法，这两部分了然于胸很重要，尤其在ai领域





# 2.21&#x20;

## 232 用栈实现队列

```python
class MyQueue:
    """
    push pop peek empty
    用列表 来模拟 栈,只能访问list[-1]，如果访问[0]就釜底抽薪了，不是队列了
    """
    def __init__(self):
        self.stack_in = [] #push
        self.stack_out = [] #pop

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        
    def pop(self) -> int:
        """
        <是 队头 |是栈底，俩在一块
        in  <|123
        out <|321
        """
        if self.stack_in:
            self.peek()
        return self.stack_out.pop()
            

    def peek(self) -> int:
        """看一眼底,和pop所需一样"""
        if self.stack_out: return self.stack_out[-1]
        if not self.stack_in: return -1
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
        

    def empty(self) -> bool:
        return not(self.stack_in or self.stack_out)


```



## 225 用队列实现栈

懒得top实现了

```python
from collections import deque

class MyStack:

    def __init__(self):
        """这里q_out只用作辅助"""
        self.q_in = deque()
        self.q_out = deque()

    def push(self, x: int) -> None:
        self.q_in.append(x)

    def pop(self) -> int:
        """
        queue_in  <|123>
        queue_out <|>

        <<popleft>> 
        queue_in  <|3>
        queue_out <|12>

        <<交换>>
        queue_in  <|12>
        queue_out <|3>
        """
        if self.empty(): return None
        for i in range(len(self.q_in) - 1):
            self.q_out.append(self.q_in.popleft())
        self.q_in,self.q_out = self.q_out,self.q_in
        return self.q_out.popleft()

    def top(self) -> int:
        if self.empty(): return None
        return self.q_in[-1]

    def empty(self) -> bool:
        return len(self.q_in) == 0

```



## 20 有效的括号

```python
class Solution:
    def isValid(self, s: str) -> bool:
        """ 
        栈很合适
        s     ()
              c       
        stack [(]
        """
        cd = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char not in cd:  #左括号
                stack.append(char)
                print(f"append {char},stack is {stack}")
            else: #右括号
                if not(stack and stack.pop() == cd[char]): return False #匹配失败 == not(遍历结束前一定有左括号垫着,且出栈应该相等)
        if len(stack) == 0:
            return True
```

## 1047 删除字符串中的所有相邻重复项

* if else逻辑可以合并，一般来讲用 if stack是好的判断

  * 只要非空，我就开始判断，否则我就append进去

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        s     abbaca
        stack a
        """
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack) 

```

# 2.22&#x20;

## 150 逆波兰表达式的值

非常简单和对对碰差不多

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ 运算符在操作数 之后"""
        def div(a,b):
            return a/b

        stack = []
        op = {'+':add,'-':sub,'*':mul,'/':div}
        res = 0
        for c in tokens:
            if c.isdigit() or (len(c)>1 and c[1].isdigit()): #isdigit不识别复数
                stack.append(c)
            else:
                b = stack.pop()
                a = stack.pop()
                # stack.append(str(int(eval(a+c+b)))) #这会很慢
                stack.append(op[c](int(a),int(b)))
        return int(stack[0])
            
```



## 239 滑动窗口最大值

deque()，用起来就是个能双端弹出( `popleft()` )的 列表，很好用

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 
        单调队列： 维护可能是最大值的队列
res     旧元素 << [3 -1 ] << 新元素

        维护: 
        1.窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作
        2.push的元素value大于入口元素的数值，那么就将队列入口的元素弹出，直到push元素的数值小于等于队列入口元素的数值为止

        注意不要提前弹出，i>=k-1时候开始
        """
        def update_sort_que(sort_q,num):
            while(sort_q and num > sort_q[-1]): sort_q.pop()
            sort_q.append(num)

        sort_q = deque()
        max_list = []
        for i in range(len(nums)): #每步加入一个，弹出一个
            update_sort_que(sort_q,nums[i])
            # print(f"after update,sort_q is {sort_q}")
            if i>=k and nums[i-k] == sort_q[0]:#弹出
                # print(f"弹出,i is {i}")
                sort_q.popleft()
            if sort_q and i>=k-1:
                # print(f"添加,i is {i}")
                max_list.append(sort_q[0]) #直接加入会溢出,
        return max_list

```



## 347 前K个高频元素



```python
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 出现频率高于k 就添加到 res中
        堆是一棵完全二叉树，树中每个结点的值都不小于（或不大于）其左右孩子的值。
        优先队列 >> 小顶堆 >> 头顶是最小的,弹出去,维护最大的在队列里
        
        堆中加入的是 元组，排序的方式是按照freq
        """
        #O(n)
        cnt_map = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            cnt_map[nums[i]] = cnt_map.get(nums[i], 0) + 1
        print(f"cnt_map is {cnt_map}")
        
        #O(m * logk) = O(n*logk) headq.headpush/headpop是O(n)
        #使用小顶堆而不是 直接对values()排序
        pri_que = []
        for key,freq in cnt_map.items():
            heapq.heappush(pri_que,(freq,key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
            print(f"pri_que is {pri_que}")

        O(k) = O(1)
        res = [0] * k
        for i in range(k-1,-1,-1): #倒着写入
            res[i] = heapq.heappop(pri_que)[1] #
        return res
        

```
