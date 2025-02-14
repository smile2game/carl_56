# 2.14 周五

## 链表基础

* head一直都是空的

  * 删除头节点的时候用 `pre_dummy_head = ListNode(next = head) `

  * 遍历时候用 `current = dummy_head.next`

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGY3NDA0MDliNjFlM2NjMzI2ZmM4MmM4YjYwMTFlNmJfdUhSTklPU2wzVHl3bnAxcW5HM09iOFJyT0hxUXB1VVpfVG9rZW46UmttVmJVcnhZb1pidnV4Q2dpRmNqTlhpbnJoXzE3Mzk1NDgyMTM6MTczOTU1MTgxM19WNA)



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

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=YWY3Y2NlMzZjODc5ZmMyYTcxZWE0Nzc3YjEzNmI0YjZfMHlkUUJvZFd2Y2JGUTl3ZGU5cmNhVDJXalBuN01BZG1fVG9rZW46S2EzamJhQlpzb1dSRDh4N3c0R2NMNTZ6bnZnXzE3Mzk1NDgyMTM6MTczOTU1MTgxM19WNA)



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
