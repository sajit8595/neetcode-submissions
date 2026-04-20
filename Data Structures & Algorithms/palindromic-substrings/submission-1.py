class Solution:
    def countSubstrings(self, s: str) -> int:

        def expandFromCenter(ind, isOdd):
            i = ind
            j = ind if isOdd else ind+1
            ans = 0
            while i >= 0 and j < n and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            return ans

        ans = 0
        n = len(s)
        for ind in range(n):
            # odd length
            ans += expandFromCenter(ind, True)
            # even length
            ans += expandFromCenter(ind, False)

        return ans