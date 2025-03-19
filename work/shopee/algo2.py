
#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param digits string字符串  
# @return string字符串一维数组
#
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.lmap = {
            "":"",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
    def bt(self,digits,startindex):
        #终止条件
        if len(self.path) == len(digits):
            self.res.append("".join(self.path[:]))
            return 
        letters = self.lmap[digits[startindex]]
        for char in letters:
            self.path.append(char)
            self.bt(digits,startindex+1)
            self.path.pop()

    def letterCombinations(self, digits) :
        # write code here
        if digits == "": return []
        self.bt(digits,0)
        return self.res


if __name__ == "__main__":
    input = "89"
    sol = Solution()
    res = sol.letterCombinations(input)
    print(f"res is {res}")
    