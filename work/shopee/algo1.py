
#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param s string字符串  
# @param t string字符串  
# @param r string字符串  
# @return bool布尔型
#
class Solution:
    def isInterleave(self, s, t, r) :
        # write code here
        i,j = 0,0
        s = list(s)
        t = list(t)
        r = list(r)
        # print(f"len(r) is {len(r)}")
        for k in range(len(r)):
            if i< len(s) and r[k] == s[i]:  
                i += 1
            elif j < len(t) and r[k] == t[j]: 
                j += 1
            else: 
                return False
        return True
    
if __name__ == "__main__":
    s = "shopee"
    t = "seamoney"
    # r = "shoseapemoneey"
    r = "shoseaepemoney"
    sol = Solution()
    flag = sol.isInterleave(s,t,r)
    print(f"flag is {flag}")