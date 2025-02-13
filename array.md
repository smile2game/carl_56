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

击败了 98%但是内存占用较多，仅击败12%

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """滑动窗口"""
        l = 0
        min_len = 1e6
        n = len(nums)
        sum = 0

        for r in range(n):
            sum += nums[r]
            while(sum >= target):
                min_len = min(min_len,r-l+1) #长度是 r-l+1
                sum -= nums[l]
                l+=1
        if min_len == 1e6:
            return 0
        else:
            return min_len
```



## 59 螺旋矩阵：

循环不变量，二分法的不变量是区间的定义，而本题螺旋矩阵的不变量是循环尺寸的含义是 max-circle

* 每圈循环的方式也不变

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """模拟"""
        res = [[0]*n for _ in range(n)]
        circle = n//2  #要画多少圈 
        print(f"circle is {circle}")
        start_row,start_col = 0,0  #起始点需要记录
        cnt = 1
        for offset in range(1,circle+1):
            for i in range(start_col,n-offset):
                res[start_row][i] = cnt 
                cnt += 1  
                # print(f"right: {res},offset is {offset},i is {i}")
            for i in range(start_row,n-offset):
                res[i][n-offset] = cnt 
                cnt += 1
                # print(f"down: {res},offset is {offset},i is {i}")
            for i in range(n-offset,start_col,-1):
                res[n-offset][i] = cnt 
                cnt += 1
                # print(f"left: {res},offset is {offset},i is {i}")
            for i in range(n-offset,start_row,-1):
                res[i][start_col] = cnt 
                cnt += 1
                # print(f"up: {res},offset is {offset},i is {i}")
            #更新起点
            start_col += 1
            start_row += 1 
        #奇数填充中心点，偶数完成循环即可
        if n%2 != 0:
            mid = n//2
            res[mid][mid] = cnt
        return res
```

耗时0ms，击败100%



## 58 carl区间和：

前缀和思想：

区间和多次查询，复杂度过高



* 要求解的是 \[a,b]左闭右闭，因此sum = presum\[b] - presum\[a-1]，同时if a == 0,防止-1越界

```python
import sys
n = int(input())
data = [0] * n
for i in range(n):
    data[i] = int(input())
# print(data)


presum = [0] * n
presum[0] = data[0]
for i in range(1,n):
    presum[i] = data[i] + presum[i-1]

# print(f"presum is {presum}")
    
for line in sys.stdin:
    a,b = map(int,line.strip().split())
    # print(f"a is {a},b is {b}")
    if a == 0:
        print(presum[b])
    else:
        print(presum[b]-presum[a-1])
```



## 44 开发商购买土地

单纯的区间求和问题，不过是二维矩阵的纵向和横向都求和

```python
#直接把全部读进来了，挺抽象的
import sys
input = sys.stdin.read #这种读法，会读到文件结束EOF
data = input().split()
n = int(data[0])
m = int(data[1])

cube = []
sum = 0 #全部总和
idx = 2 #从下标为2开始
for i in range(n):
    row = []
    for j in range(m):
        num = int(data[idx])
        idx += 1
        row.append(num)
        sum += num
    cube.append(row)
# print(f"cube is {cube}")

#行的和
horizontal = [0] * n
for i in range(n):
    for j in range(m):
        horizontal[i] += cube[i][j]
#列的和
vertical = [0] * m
for j in range(m):
    for i in range(n):
        vertical[j] += cube[i][j]

#求解一刀切的结果
result = float('inf')
horizontalCut = 0
for i in range(n):
    horizontalCut += horizontal[i]
    result = min(result, abs((sum - horizontalCut)-horizontalCut))
    
verticalCut = 0
for i in range(m):
    verticalCut += vertical[i]
    result = min(result, abs((sum - verticalCut)-verticalCut))
    
print(result)
```







# 基础技巧：

## for和while的区别

* for循环自动会给i +=1，但是for循环一旦进入，其上届不会变，不像while能够until



## 简单但是慢的操作：

采用提前申请好数组并用下标访问，能大幅提升速度

* append(value)

* insert(index,value)







## cpp的输入输出

```python
#输入
scanf("%d", &vec[i]);
cin >> vec[i];

#输出
printf("%d\n", sum);
cout << sum << endl;
```
