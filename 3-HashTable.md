## 基础知识

hash就是一个特殊的映射，多用作出现次数映射



* 场景：

快速判断一个元素是否出现集合里的时候，就要考虑哈希法。

牺牲了空间换取了时间，因为我们要使用额外的数组，set或者是map来存放数据，才能实现快速的查找。



* Hash table： index >> hashCode (可以代表出现的次数)

* Hash function: name >> index

数组就是简单的hash表

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=NDkyZTcxMzAwMWQzODBiZGI3ZDg1ZTMyMWE1MTI0MDRfWnBEbE9YZ2RFMTlKUDdUbnBvdmRqOEgycFRlTmtzNkFfVG9rZW46SE9NZGJ0RWZIbzk0cGl4bDBWdGNLSGFzbkxjXzE3Mzk4OTE5Mjc6MTczOTg5NTUyN19WNA)

```python
index  = hashFunc(name)
hashFunc = hashCode(name) % tableSize
```

### 碰撞及解决



解决方案：

* 拉链法&#x20;

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=MGY2YTc1ODdiZWI1MGU3MDE2ZmNkM2FkYTY3YWMxMjlfSzdKU052aGxaVm00VzcwR2xUVXkwenRZcmxqb3owSW1fVG9rZW46STlFY2JVa0o0b0YxdHZ4bks1ZmM1aTJsbkZoXzE3Mzk4OTE5Mjc6MTczOTg5NTUyN19WNA)

* 线性探测法

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2MwNGY1NDZiYTc2N2Q2Yzc2MTc2NjgxYjQxNzgzMTlfeDVxSGxMa0RNa1M3dTNEMHlzWVM5NHJPQW1HNUZFVVpfVG9rZW46SmFYRWJybE4zbzZaZ2Z4UDhHN2NqdUdFbm5oXzE3Mzk4OTE5Mjc6MTczOTg5NTUyN19WNA)



### 功能函数：

![](https://o0rjrextel0.feishu.cn/space/api/box/stream/download/asynccode/?code=NDU5YjhiYjJmZWNhNjQ5MzVjNjczMmU3N2I5NWIyZTBfdEFDYWJNTTJ1aURyRllEOThmc09XNXRXdFo2eGpEeUpfVG9rZW46VDZ6Y2JnWElub0FZbEx4a0Q0WWM0MTY0bnhnXzE3Mzk4OTE5Mjc6MTczOTg5NTUyN19WNA)

python中,

* 对应unordered\_set的是 set

  * 无序、唯一元素的集合，基于哈希表实现。

  * 常用操作：`add()`, `remove()`, `in` 关键字（判断元素存在性）。

```python
s = set()
s.add(1)
s.add(2)
print(3 in s)  # 输出: False
```

* 对应unordered\_map的是dict

```python
d = {}
d["apple"] = 5
d["banana"] = 3
print("apple" in d)  # 输出: True
```



# 周一 2.17

## 242 有效的字母异位词

* 简单的用数组实现

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """异位词 >> 重新排列"""
        record = [0] *26
        for i in s:
            index = ord(i) - ord('a')
            record[index] +=1
        for i in t:
            index = ord(i) - ord('a')
            record[index] -=1
        for num in record:
            if num != 0:
                return False
        return True
```



## 349 两个数组交集

* 注意python中数据结构的选择

定长度就用 数组

不定长度就用dict

值唯一且无需就用set

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        不限制数值的大小，无法用数组来做了,要用dict
        但是dict比数组慢占用空间多
        """
        # table = [] #数组长度不可变，不知道搞多大的
        # table = set() #set没有下标，解决不了这种 table[num] = cnt的问题

        table = {}
        for num in nums1:
            table[num] = table.get(num,0) + 1 #获取num的出现次数，没有就返回0，+1、
        
        res = set() #set具有唯一性质
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        return list(res) #返回一个列表

```



## 202 快乐数

有没有用set，查具体几个用dict





* set的api，`add,in`

* dict的api，`get`

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            n = self.getSum(n)
            if n == 1:
                return True
            else:
                if n in record:
                    return False
                else:
                    record.add(n)

    def getSum(self,n):
        bit2_sum = 0 
        while  n:
            n,r = divmod(n,10)
            bit2_sum += r **  2
        return bit2_sum
```



## 1 两数之和

判断target - value是否在，在的话，在哪里

1. 长度不定不用数组

2. 需要下标不用set

3. dict&#x20;

   1. hashtable\[value] = index

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """find target - x : O(n) >> O(1) ,要用hashtable才能实现这个优化"""
        hashtable = dict() # hashtable[value] = index
        for index,value in enumerate(nums):
            if target - value in hashtable: #这里是查询他的key
                return [hashtable[target - value],index]
            else:
                hashtable[value] = index
        return []

```

# 周二 2.18&#x20;

## 454 四数相加2

求几数之和问题，不考虑有重复的四个元素相加等于0的情况，用哈希就很简单

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        两个数组分成一组
        dict 表示出现次数
        """
        sum_cnt = dict() # {sum : cnt} 
        for num1 in nums1:
            for num2 in nums2:
                sum_cnt[num1 + num2] = sum_cnt.get(num1 + num2,0) + 1
        
        cnt = 0
        for num3 in nums3:
            for num4 in nums4:
                sum34 = num3 + num4 
                if (0-sum34) in sum_cnt:
                    cnt += sum_cnt[0-sum34]
        return cnt
```



## 383 赎金信

字母统计够不够用的，都是26个字母就用数组就够用

* Record\[w] = cnt

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26 #字母题就用有限的数组就可以
        for w in magazine:
            record[ord(w) - ord('a')] += 1
        print(f"record is {record}")

        for w in ransomNote:
            record[ord(w) - ord('a')] -= 1
            if record[ord(w) - ord('a')] < 0:
                return False
        return True
```



## 15 三数之和

暴力是 O(n3)，确实暴力的时间复杂度上升了，脑子的内存也占用大

### Hash + 去重

过于麻烦了，也没有完全搞明白，给出一个debug版本

O(n2) 是必须的，最后能够用hash，if c in d: 将O(n) >> O(1)

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        很讨厌的数组题先排个序
        有重复数字了,不能用set，要用dict
        三元组内部也不能重复, 去重很难的
        """
        result = []
        nums.sort()
        print(f"排序后:nums = {nums}")
        # 找出a + b + c = 0
        # a = nums[i], b = nums[j], c = -(a + b)
        for i in range(len(nums)):
            # 排序之后如果第一个元素已经大于零，那么不可能凑成三元组
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: #三元组元素a去重
                print(f"a重复,nums[i] == nums[i - 1] 为 {nums[i]} == {nums[i - 1]},i = {i}")
                continue
            d = {} # { value : index } 
            for j in range(i + 1, len(nums)):
                print(f"内循环,i is {i},j is {j}")
                if j > i + 2 and nums[j] == nums[j-1] == nums[j-2]: # 三元组元素b去重
                    print(f"b重复,j is {j},nums[j] is {nums[j]},nums[j-1] is {nums[j-1]},nums[j-2] is {nums[j-2]}")
                    continue
                #hash
                c = 0 - (nums[i] + nums[j])
                print(f"before,d is {d}")
                if c in d:
                    print(f"存在{c} in {d},nums[i] is {nums[i]},nums[j] is {nums[j]},c is {c}")
                    result.append([nums[i], nums[j], c])
                    d.pop(c) # 三元组元素c去重
                    print(f"d is {d}\n")
                else:
                    d[nums[j]] = j
                    print(f"{c}在d中不存在,d[nums[j]] is {d[nums[j]]},j is {j}")
                    print(f"d is {d}\n")
        return result
```

### 双指针

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        求和题目,无限长度，用dict，如果用hash

        双指针: k指针O(n)，但是ij指针双向奔赴O(n),所以总体是 O(n2)
        k  i  j,停留在重复的第一个数字 
        for k: 
            for i:
                for j： 
        """
        res = []
        nums.sort()
        print(f"排序后:nums = {nums}")
        for k in range(len(nums)):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue #如果没有k>0在前面就会 前越界
            i,j = k+1 , len(nums) - 1
            while (i<j): #双指针
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i+=1
                    while(nums[i] == nums[i-1] and i < j):
                        print(f"i is {i},nums[i] is {nums[i]}")
                        i+=1 
                elif s > 0:
                    j-=1
                    while(nums[j] == nums[j+1] and i < j): #如果和自己移动的前一步一样的话,就接着走
                        print(f"j is {j},nums[j] is {nums[j]}")
                        j-=1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i +=1
                    j -=1
                    while i < j and nums[i] == nums[i-1]: i+=1
                    while i < j and nums[j] == nums[j+1]: j-=1
        
        return res
```



## 18 四数之和

三数之和外面多套了一层循环，到最后两层时候用双指针求两数之和

太简单了

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """ 不能重复 """
        nums.sort() 
        n = len(nums)
        res = []
        for i in range(n-3): # 外层循环, a: n-4, b:n-3,c: n-2,d: n-1 
            a = nums[i]
            if i >0 and nums[i-1] == nums[i]: #去重,前身已经遍历过了，直接跳过这个
                continue
            for j in range(i+1,n-2):
                b = nums[j]
                if j > i+1 and nums[j-1] == nums[j]: #去重,前身已经遍历过了，直接跳过这个
                    continue
                #优化 跳过
                #双指针开始,又回到原来了
                l = j + 1 
                r = n - 1
                while(l<r):
                    s = a+b + nums[l] + nums[r]
                    if s > target:
                        r -=1
                    elif s < target:
                        l +=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while l<r and nums[l-1] == nums[l]:
                            l +=1 
                        r-=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
        return res
```



# 总结：

1. hash本身是一种特殊的映射，通过 **哈希函数（Hash Function）**&#x5C06; **输入（如字符串、数字**等）转换为固定长度的**数值（哈希值）**，并**基于此数值直接定位到存储位置**。

2. 适用范围： 求和、求是否出现过、以及次数是否足够

3. 数据结构选择：(映射:x -> y)

   * 数组：有限的x数据, 例如字母&#x20;

   * Dict ：无限的x数据，例如int数字出现次数

4. hash和双指针，都能把两数之和 O(n2) >> O(n)，三数之和和四数之和就是往外面套for循环，不难

