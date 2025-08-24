class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_l = 0

        for i in range(n + n -1):
            if i %2 == 0: #字符中心
                l,r = i//2,i//2 #l,r始终指向 字母
            else: #间隙中心
                l = i//2
                r = i//2 +1 
            while l>=0 and r<n and s[l] == s[r]: #不断扩展
                l -=1
                r +=1

            if r-l-1 > max_l:
                max_l = r-l-1
                res = s[l+1:l+max_l+1]
            # print(f"res is {res}")
        return res

