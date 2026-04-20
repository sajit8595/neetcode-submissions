class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        n = len(s)
        for ind in range(n):
            # odd length
            i, j = ind, ind
            while i >= 0 and j < n and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1

            # even length
            i, j = ind, ind+1
            while i >= 0 and j < n and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
                
        return ans