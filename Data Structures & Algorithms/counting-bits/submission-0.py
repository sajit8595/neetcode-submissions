class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n+1)]
        for ind in range(1, n+1):
            if ind&1:
                dp[ind] = dp[ind-1] + 1
            else:
                dp[ind] = dp[ind >> 1]
        return dp