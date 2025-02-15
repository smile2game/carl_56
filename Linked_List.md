# 总结：

1. 做链表题一定要画图：

* 普通标准链表

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2E2YTVhMDdlNGVlOTMwMmE0YmM2MDcwODY0NGJjODFfVkpiRnNuVFl4Q1NUeExFSmZQYzBBVjVJZEs5cmEwR3ZfVG9rZW46V1ZzWWJSamp3b1hmTjR4TGdYY2NjZFgxbkxnXzE3Mzk2MzIzMzk6MTczOTYzNTkzOV9WNA)

* 虚拟头节点

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=NDYwMjc0ZGJmNTVhYWUzYzEwNzhjNmNmY2M5ZGRkZTRfa01YRmplT29GRjJrTmVnUHVJNFpHSkxkdzdJaG8wWlZfVG9rZW46UHRhWGJ5eG5Qb2FoWFh4Um5oZmM2dU5SbkhlXzE3Mzk2MzIzMzk6MTczOTYzNTkzOV9WNA)



* 边界条件确实是难点：

- while的终止条件要保证：最后一次操作直到结束都不会None.next/val&#x20;

  1. `While cur.next and cur.next.next:`

- while内部：

  1. 放置tmp保留节点

  2. 交换

  3. 移动current



* 链表非常简单的debug方式：

```python
print(f"dummy_head.next is {dummy_head.next}")
```



3. 双指针比我想得用的还要多，快慢指针找环，很有意思。

# 2.14 周五

## 链表基础

* head一直都是空的

  * 删除头节点的时候用 `pre_dummy_head = ListNode(next = head) `

  * 遍历时候用 `current = dummy_head.next`

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=YjUzZmNkNTlmM2NlYzY5YzJkOTA1Y2Q2NzUwNmQyOWFfUmt2dFJXbjNLYjhyNXU5c1JDejd1cGxjWTlycHp4enZfVG9rZW46UmttVmJVcnhZb1pidnV4Q2dpRmNqTlhpbnJoXzE3Mzk2MzIzMzk6MTczOTYzNTkzOV9WNA)



### 链表操作

* 定义：

```python
#单向，包含值和指针
class ListNode:
    def __init__(self.val,next = None):
        self.val = val
        self.next = next
```

* 添加

```python
A -> B -> C
#前面和当前的 ListNode改next
A -> D -> B -> C
```

* 删除

  * 前一个节点直接指向他后面的跳过他

  * 删除头节点，将头节点往后移动一位



python有内存回收机制，不用手动释放

### 性能分析：

* 链表更适合插入，长度不定

* 数组更适合查询，长度固定

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=NThkNzRhYzYzNjIyMzAyOWFlNTUxYjQ2NGVhMTk3Y2ZfQlVJWUtzTVhhQ3JlUWtzMkhQNkppaFhQdkFmbmd4RkJfVG9rZW46S2EzamJhQlpzb1dSRDh4N3c0R2NMNTZ6bnZnXzE3Mzk2MzIzMzk6MTczOTYzNTkzOV9WNA)



## 203  移除链表元素

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """需要把head初始化出来才不会Nonetype，直接print(head.val)时候会报错
        初始化新节点时候,只需要提供next即可,val默认是0.   dummy在头之前用来删除头节点
        """        
        dummy = ListNode(next = head) 
        # print(f"dummy is {dummy}")
        current = dummy  #遍历用
        while current.next:
            if current.next.val == val:
                current.next = current.next.next #删除
            else:
                current = current.next #移动
        return dummy.next

```



## 707 手动链表



* get时候` for i in range(index)`

* AddTail时候 `while current.next !=None:`

* AddAtIndex和Delete时候 `for i in range(index -1 ):`

```python
class ListNode:
    """节点"""
    def __init__(self,val = 0,next = None):
            """初始化"""
            self.val = val
            self.next = next

class MyLinkedList:
    def __init__(self):
        """初始化整根链和头"""
        self.dummy_head = ListNode() #
        self.size = 0 #维护尺寸，防止越界

    def get(self, index: int) -> int:
        """根据下标获得值
        myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
        myLinkedList.get(1);              // 返回 2 (移动一次current就到了)
        """
        if index < 0 or index >=self.size:
            return -1
        current = self.dummy_head.next #从节点开始访问
        for i in range(index):
            current = current.next
            print(f"get,i is {i},current.val is {current.val}")
        return current.val

    def addAtHead(self, val: int) -> None:
        """头插入"""
        self.dummy_head.next = ListNode(val,next = self.dummy_head.next) #赋值语句先执行后面的命令
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """尾插入"""
        current = self.dummy_head.next
        while current.next != None:
            current = current.next
        current.next = ListNode(val = val)
        self.size += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        """index插入"""
        current =self.dummy_head.next
        for i in range(index-1):
            current = current.next
        current.next = ListNode(val = val,next = current.next)
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        """"删除"""
        current =self.dummy_head.next
        for i in range(index-1):
            current = current.next
        current.next =  current.next.next
        self.size -= 1 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```



## 206 反转链表

源码：

```python
     pre     cur  pre
null(head) -> 1 -> 2 -> 3 -> 4 -> 5 -> null -> null
                            pre  cur    tmp
                                 pre    cur    tmp    
```

解法：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head #这个是实际的头节点，不是虚拟头节点
        print(f"cur.val is {cur.val},cur.next is {cur.next}")
        pre = None
        while cur: #最后一次满足条件是 cur指向 5,执行完cur 在None(直接是空,无关链表了)，而pre指向5
            tmp = cur.next 
            #反转pre->cur为 pre<-cur
            print(f"cur.val is {cur.val}")
            cur.next = pre 
            #指针指到位
            pre = cur
            cur = tmp
        return pre
        

```





# 2.15 周六

## 24 两两交换链表节点



* 普通：

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        cur = dummy_head
        while cur.next and cur.next.next: #条件
            print(f"cur.val is {cur.val}") #证明是跳着走的
            #init tmp
            tmp = cur.next
            tmp1 = cur.next.next.next
            print(f"Before,dummy_head.next is {dummy_head.next}")
            #swap
            cur.next = cur.next.next
            cur.next.next = tmp
            tmp.next = tmp1
            #go
            cur = tmp
            print(f"After,dummy_head.next is {dummy_head.next}")
        return dummy_head.next

```



* 递归版本：

```python
#回来再写
```



## 19 删除链表中倒数第N个节点：

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=YTFlMTcwODUxMmFlNzY2ZWYyMWQ3MTE0MGJkMTBiMDdfdFlaTU9PeVN0ZHpuQmtWbnViOVNpQWczRGtCWDRDOFpfVG9rZW46T1l4SmJKNkJVb0h6RnF4cWVJUWNVZHJlbkloXzE3Mzk2MzIzMzk6MTczOTYzNTkzOV9WNA)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """难点是 怎么把指针放到 要删除的那个位置"""
        dummy_head = ListNode(next = head)
        slow,fast = dummy_head,dummy_head
        #预走fast
        for i in range(n+1):
            fast = fast.next
        #一起走
        while fast:
            fast = fast.next
            slow = slow.next
            print(f"slow.val is {slow.val}")
        slow.next = slow.next.next
        return dummy_head.next #注意这里返回的是dummy_head.next而不是head(因为dummy_head)

```





## 面试题 02.07 链表相交

通过长度来决定从哪里开始，同时遍历后面可能是交点的节点 O(n)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """末端对齐，检测交点指针从哪里开始"""
        lenA,lenB = 0,0
        #统计长度
        curA,curB = headA,headB
        while curA:
            lenA +=1 
            curA = curA.next
        while curB:
            lenB +=1 
            curB = curB.next
        print(f"lenA is {lenA},lenB is {lenB}")
        
        # 调整长链的开始指针
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        else:
            for i in range(lenB-lenA):
                curB = curB.next
        while curA:
            print(f"curA is {curA},curA.val is {curA.val}") #可以看到真正的相等除了val相等，后面的ListNode也需要全部相等的
            print(f"curB is {curB},curB.val is {curB.val}")
            if curA == curB:
                print("上面==")
                return curA
            else:
                print("上面!=")
                curA = curA.next
                curB = curB.next
        return None
```



## 142 环形链表2&#x20;

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针来找到环,快指针走两步慢指针走一步
        >> 链表长度为 a + b,a是单线长度,b是环的周长,
        >> f和s代表快慢指针走的路程,能够相遇则f = s + nb，因为前面的a都是一起走的，后面一定是多出了整圈
        l = a + b 
        f = 2s 
        f = s + nb 
        >> 相减得到s表达式
        f = 2nb
        s = nb
        >> k表示从头然后经过任意圈到入口的指针，找到k就行了，s再走a步就会成为k,也就是入口
        k = a + nb 
        s = nb 
        >> 只要让slow再走a步就可以了，构建指针和slow一起走
        slow + a == head + a  
        """
        f,s = head,head
        while True: #直到
            if f == None or f.next == None:
                return None
            f = f.next.next
            s = s.next
            if f == s:
                break
        
        k = head
        while k!=s:
            k = k.next
            s = s.next
        return s
```

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=Nzc1YjBlY2NmZDRjMzcwYmVmMzFlM2E1ZGYyMzljNTVfMVVhR2FtYUpMZXByaFFDSlRYdktjV3FuNmlPRDdLQW5fVG9rZW46R2s5TGI4TFJrb2VkMmp4ZHZXbWNzZlFsbjdlXzE3Mzk2MzIzMzk6MTczOTYzNTkzOV9WNA)

