class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r, startInd, maxLen):
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    startInd = l
                l -= 1
                r += 1
            return [startInd, maxLen]


        n = len(s)
        startInd = 0
        maxLen = 0
        
        for i in range(n):
            # odd len
            startInd, maxLen = expand(i, i, startInd, maxLen)
            # even len
            startInd, maxLen = expand(i, i+1, startInd, maxLen)         

        return s[startInd : startInd+maxLen]

