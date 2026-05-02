class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l, r):
            ans = 0
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            return ans
        
        ans = 0
        for i in range(n):
            ans += expand(i, i)
            ans += expand(i, i+1)
        return ans