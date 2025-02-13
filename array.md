# 2.12 周三

## 704 二分查找（左闭右闭）

适用条件：

1. 顺序

2. 唯一

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            middle = (l+r)//2
            print(f"l is {l},r is {r},middle is {middle},nums[middle] is {nums[middle]}")
            if target < nums[middle]:
                r = middle - 1 
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
            print(f"After adapt!! l is {l},r is {r}")
        print(f"after all! middle is {middle},l is {l},r is {r}")
        return -1 

```



## 27 移除元素

暴力法

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """for循环不行，因为外圈循环l需要更新，所以外圈用while"""
        i, l = 0, len(nums)
        while i < l:
        # for i in range(l): #这个时候的l并不会变了，是一开始就生成好的
            if nums[i] == val: # 找到等于目标值的节点
                print(f"==搬运,i is {i},l is {l}")
                for j in range(i+1, l): # 移除该元素，并将后面元素向前平移
                    nums[j - 1] = nums[j]
                    print(f"内,i is {i},j is {j},l is {l}")
                l -= 1
                i -= 1
                print(f"--搬运完成,i is {i},l is {l}")
            print(f"外圈,i is {i},l is {l},nums is {nums}")
            i += 1
        return l
```



快慢指针：

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        快慢指针
        fast -> 搜索指针,寻找新数组
        slow -> 新数组指针
        if nums[fast] != val: # 只要不等于目标值，就搬过来,否则跳过去
            nums[slow] != nums[fast] 
        """
        slow = 0
        for fast in range(len(nums)):
            print(f"==slow is {slow},fast is {fast},nums[:slow] is {nums[:slow]}") #这个fast怎么从1开始?
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
                print(f"----slow is {slow},fast is {fast},nums[:slow] is {nums[:slow]}")
        
        for i in range(3):
            print(f"i is {i}")
        return slow

```



## 979 有序数组的平方

用时击败5%

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        双指针，对向而行，而非快慢指针
        """
        res = []
        l,r = 0,len(nums)-1
        for i in range(len(nums)):
            l2 = nums[l]*nums[l]
            r2 = nums[r]*nums[r]
            if l2 > r2:
                res.insert(0,l2)
                l+=1
            else:
                res.insert(0,r2)
                r-=1
            # print(f"l2 is {l2},r2 is {r2},res is {res}")
        return res
```



用时 击败69%，insert还是慢，预先申请好的快

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        双指针，对向而行，而非快慢指针
        """
        res = [0] * len(nums)
        l,r = 0,len(nums)-1
        for i in reversed(range(len(nums))):
            l2 = nums[l]*nums[l]
            r2 = nums[r]*nums[r]
            if l2 > r2:
                res[i] = l2
                l+=1
            else:
                res[i] = r2
                r-=1
            # print(f"l2 is {l2},r2 is {r2},res is {res}")
        return res

```

# 2.13 周四

## 209 长度最小的子数组

滑动窗口 （特殊的双指针）

for循环表示 终止位置，如果初始位置就需要往后 O(n2)了



三要素：

* 窗口内是什么

* 何时移动初始位置

* 何时移动结束位置



针对本题：

* 窗口内：满足和 >= s的最小子数组

* 起始位置移动：>s了就要缩小

* 结束位置移动：遍历



时间复杂度O(n)，因为wihile(sum >= s)是k，不是n

```python
```
