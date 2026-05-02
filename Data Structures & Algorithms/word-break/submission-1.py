class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for ind in range(n-1, -1, -1):
            for w in wordDict:
                wn = len(w)
                if ind + wn <= n and s[ind : ind+wn] == w:
                    dp[ind] = dp[ind+wn]
                if dp[ind]:
                    break
        return dp[0]