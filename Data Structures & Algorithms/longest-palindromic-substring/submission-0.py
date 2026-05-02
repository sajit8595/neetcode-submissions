class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        startInd = 0
        maxLen = 1
        dp = [[False for j in range(n)] for i in range(n)]
        # length = 1
        for i in range(n):
            dp[i][i] = True
        # length = 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxLen = 2
                startInd = i
        # length >= 3
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j =  i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    maxLen = length
                    startInd = i
        return s[startInd: startInd+maxLen]

