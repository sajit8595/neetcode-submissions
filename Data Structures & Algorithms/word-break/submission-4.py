class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        n = len(s)
        def recur(ind, prevInd):
            if ind == n:
                return s[prevInd:ind] in wordSet
            
            key = (ind, prevInd)
            if key in memo:
                return memo[key]

            op1 = False
            if s[prevInd:ind] in wordSet:
                op1 = recur(ind, ind)
            op2 = recur(ind+1, prevInd)

            memo[key] = op1 or op2
            return memo[key]
        
        return recur(0, 0)