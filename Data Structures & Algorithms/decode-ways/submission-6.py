class Solution:
    def __init__(self):
        self.n = -1

    def decodeWays(self, ind, s):
        if ind == self.n:
            return 1
        if ind == self.n-1:
            return 1 if s[ind] != '0' else 0

        ans = 0
        if '1' <= s[ind] <= '9':
            ans += self.decodeWays(ind+1, s)
        if '1' <= s[ind] <= '2':
            ans += self.decodeWays(ind+2, s)
        return ans
        
    def numDecodings(self, s: str) -> int:
        self.n = len(s)
        # return self.decodeWays(0, s)

        dp = [0 for i in range(self.n+1)]
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0

        for ind in range(self.n-2, -1, -1):
            ans = 0
            oneStep = int(s[ind])
            if 1 <= oneStep <= 9:
                ans += dp[ind+1]
            twoStep = int(s[ind] + s[ind+1])
            if 10 <= twoStep <= 26:
                ans += dp[ind+2]
            dp[ind] = ans
        return dp[0]


        