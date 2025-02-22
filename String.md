# 总结：

* list(s) 能解决大部分问题，善用切片和赋值

* 双指针太好玩了，能优化O(n2)，还能原地修改数组

  * 如果定义明确，给左右指针l,r起实际意义名字更好理解

* s.insert



* 还是跟着卡哥的文字平趟过去最顺利



# 2.19 周三

## 344 反转字符串

* 双指针，注意省略掉tmp的方式

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0,len(s)-1

        while l < r:
            s[l],s[r] = s[r],s[l] #这里省去了tmp
            l +=1 
            r -=1
        
```



## 541 反转字符串2

* 注意 `''.join(s)和 str(s)的不同`

没有额外符号的字符串（如 "abc"），使用 `''.join(s)`；而如果你想要获取列表的结构表示（如 `['a', 'b', 'c']`），则使用 `str(s)`



* 只有转化为list才能用slice and assignment

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for  i in range(0,len(s),2*k):
            s[i:i+k] = s[i:i+k][::-1]
            print(f"翻转一次: s is {s}")
        return ''.join(s)
```



## Carl 54 替换数字

不考虑原地

```python
s = input()
# print(s)
res = []
for char in s:
    if char.isdigit():
        res.append("number")
    else:
        res.append(char)
print("".join(res))
```

考虑原地：

* 双指针能解决掉for 循环一旦开始，上限就不能变的问题

* s.inert()简化了插入，不用倒着来了

```python
s = input()
# print(s)
s = list(s)
n = len(s)
i,r = 0,0 #i是原字母,r是新下标
for i in range(n):
    if s[r].isdigit():
        s[r] = 'n'
        s.insert(r+1,'u')
        s.insert(r+2,'m')
        s.insert(r+3,'b')
        s.insert(r+4,'e')
        s.insert(r+5,'r')
        r += 5
    r += 1
    # print(f"迭代到{i}次,r is {r},s is {s}")
        
print("".join(s))
        
    
```





# 2.20 周四

## 151 字符串反转

* " ".join() 表示以空格为间隔join这些单词呢

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """双指针 单词间 反转"""
        words = s.split()
        l,r = 0,len(words) -1 
        while l < r:
            words[l],words[r] = words[r],words[l]
            print(f"words[l] is {words[l]},words[r] is {words[r]}")
            l+=1
            r-=1
        return " ".join(words) #这里是说用" "作为间隔
```



## Carl 55 右旋字符串

```python
n = int(input())
s = input()
r = len(s) - n
#分两段，交换两段
s = list(s)
s = s[r:] + s[:r]
print(''.join(s))
```



## 28 找出字符串中第一个匹配项

KMP



```python
class Solution:
    def getNext(self, next, s):
        """next[i]: 下标i之前,前缀和后缀共同长度有多长
        关键定义：
        1. next[0] = 0是因为0的前后缀最大长度一定是0，所以是0()。(说明:前缀不能包含最后一个字母，后缀不能包含第一个字母)
        2. 为什么!=的回退是 j = next[j-1]呢？ >>>> 因为当前的 s[j] != s[i]，所以要找前一个的next，如果还找当前的next，那么根据next的定义，从后缀跳到前缀又会不相等，那么将永远不出来
        3. 为什么求next时候j总是落后i一位呢？ >>>> 实际上并非一直落后一位，只是开始时候形成错差，避开重叠而已。(注意next[i] = j)
        4. 为什么while时会有 j>0? >>> j=0时候即使不等也无需跳转，因为next[0] = 0,如果不规避这种情况会陷入死循环。(如果j一直为0，则i就一直往后走到头了)
        5. 求haysteck和needle时候无需落后，从0开始
-------------------------------------------
getNext:
eg1:
            i
        aabaaf
index   012345
         j
next    010

eg2:    
          i
        bad
        012
        j
-------------------------------------------
haystack == needle:

             j
        aabaabaafa
        aabaaf
          i
next    010120
        """
        print(f"\n-------求解next数组------\n")
        j = 0
        next[0] = j
        for i in range(1, len(s)):
            print(f"i is {i}")
            while j > 0 and s[i] != s[j]:
                print(f"!=,j = next[{j -1}] = {next[j-1]}")
                j = next[j -1] 
            if s[i] == s[j]:
                j += 1
                print(f"==,j+=1 is {j}")
            print(f"next[{i}] = {j}\n")
            next[i] = j
    
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        print(f"next is {next}")
        print(f"\n-------求解strstar------\n")
        j = 0
        for i in range(len(haystack)):
            print(f"i is {i}")
            while j > 0 and haystack[i] != needle[j]:
                print(f"j is {j}")
                print(f"!=,j = next[{j -1}] = {next[j-1]}\n")
                j = next[j - 1]
            if haystack[i] == needle[j]:
                print(f"j is {j}")
                j += 1
                print(f"==,j+=1 is {j}\n")
            if j == len(needle):
                print(f"找到匹配字符串")
                return i - (len(needle) - 1)
        return -1
```





## 459 重复的子字符串

## 移动匹配

```python
```



### KMP

```python
```



### find解法

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """ 
        A: s是重复子串 
        <必要性 == 充分性>     
        B: s in sx2 and s not (s[1] or s[-1])

        KMP:
        最长相等前后缀不包含的子串一定是字符串s的最小重复子串

        太抽象了,放弃了，理解不了
        """
        ss = s[1:] + s[:-1]
        print(ss.find(s))
        if ss.find(s) == -1: #-1就是没找到
            return False
        else:
            return True
        
```
