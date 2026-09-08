class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLen = 1
        self.st = 0

        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > self.maxLen:
                    self.maxLen = r - l + 1
                    self.st = l
                l -= 1
                r += 1
            
        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        
        return s[self.st : self.st + self.maxLen]
