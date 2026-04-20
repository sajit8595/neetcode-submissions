class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        d = set()
        ans = 0
        while j < n:
            while s[j] in d:
                d.remove(s[i])
                i += 1
            d.add(s[j])
            ans = max(ans, j - i + 1)
            j += 1
        return ans
