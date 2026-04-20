class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0]*(n+1)
        # 0th pos i.e length 1, will always be one, as s[0] == '0' resolved
        dp[0] = dp[1] = 1
        for ind in range(2, n+1):
            takeOne = takeTwo = 0
            if s[ind-1] != '0':
                takeOne = dp[ind-1]
            if 10 <= int(s[ind-1-1]+s[ind-1]) <= 26:
                takeTwo = dp[ind-2]
            dp[ind] = takeOne + takeTwo
        return dp[n]

        # def recur(ind):
        #     if ind < 0:
        #         return 1
        #     takeOne = takeTwo = 0
        #     if ind >= 0 and s[ind] != '0':
        #         takeOne = recur(ind-1)
        #     if ind >= 1 and 10 <= int(s[ind-1]+s[ind]) <= 26:
        #         takeTwo = recur(ind-2)
        #     return takeOne + takeTwo
        
        # return recur(len(s)-1)