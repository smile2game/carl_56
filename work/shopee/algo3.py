class Solution:
    def __init__(self):
        self.path = ""
        self.res = []
        self.flag = False
    def bt(self,word,word_dict,startindex):
        print(f"self.path is {self.path}")
        if len(self.path) > len(word):
            return
        if len(self.path) == len(word) and self.path ==  word:
            self.flag = True
            print(f"满足了")
            return
        
        for k in range(startindex,len(word_dict)):
            self.path = self.path + word_dict[k]
            self.bt(word,word_dict,startindex+1)
            self.path = self.path[:len(self.path)-len(word_dict[k]) -1]
    def wordConcate(self, word, word_dict):
        # 回溯来做
        self.bt(word,word_dict,0)
        return self.flag
    

    
if __name__ == "__main__":
    word = "shopeegarena"
    word_dict = ["shopee","garena","seamoney"]
    sol = Solution()
    flag = sol.wordConcate(word, word_dict)
    print(f"flag is {flag}")