class Solution:
    def __init__(self):
        self.n = -1

    def decodeWays(self, ind, s):
        if ind == self.n:
            return 1
        ans = 0
        oneStep = int(s[ind])
        if 1 <= oneStep <= 9:
            ans += self.decodeWays(ind+1, s)
        if ind+1 < self.n:
            twoStep = int(s[ind] + s[ind+1])
            if 10 <= twoStep <= 26:
                ans += self.decodeWays(ind+2, s)
        return ans
        
    def numDecodings(self, s: str) -> int:
        self.n = len(s)
        # return self.decodeWays(0, s)
        # if s[0] == '0':
        #     return 0

        dp = [0 for i in range(self.n+1)]
        dp[self.n] = 1
        for ind in range(self.n-1, -1, -1):
            ans = 0
            oneStep = int(s[ind])
            if 1 <= oneStep <= 9:
                ans += dp[ind+1]
            if ind+1 < self.n:
                twoStep = int(s[ind] + s[ind+1])
                if 10 <= twoStep <= 26:
                    ans += dp[ind+2]
            dp[ind] = ans
        return dp[0]


        