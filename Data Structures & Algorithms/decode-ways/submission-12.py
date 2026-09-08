class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        memo = {}
        def recur(ind):
            if ind == n:
                return 1
            if ind > n:
                return 0
            
            if ind in memo:
                return memo[ind]

            ways = 0
            if s[ind] == '0':
                return 0
            if s[ind] == '1':
                ways += recur(ind+2)
            if s[ind] == '2' and ind+1 < n and s[ind+1] in '0123456':
                ways += recur(ind+2)
            ways += recur(ind+1)
        
            memo[ind] = ways
            return memo[ind]
        
        return recur(0)
