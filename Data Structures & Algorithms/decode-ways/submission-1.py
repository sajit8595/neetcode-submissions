class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        def recur(ind):
            if ind < 0:
                return 1
                
            takeOne = takeTwo = 0
            if ind >= 0 and s[ind] != '0':
                takeOne = recur(ind-1)
            if ind >= 1 and 10 <= int(s[ind-1]+s[ind]) <= 26:
                takeTwo = recur(ind-2)

            return takeOne + takeTwo
        
        return recur(len(s)-1)