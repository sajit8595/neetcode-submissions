class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        n = len(s)
        ans = 0
        for char in set(s):
            i, j = 0, 0
            n = len(s)
            nk = 0
            while j < n:
                if s[j] == char:
                    j += 1
                elif nk < k:
                    j += 1
                    nk += 1
                else:
                    ans = max(ans, j - i)
                    if s[i] != char:
                        nk -= 1
                    i += 1
            ans = max(ans, j-i)
        return ans