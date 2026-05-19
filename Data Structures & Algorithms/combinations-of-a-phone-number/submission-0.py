class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        t9 = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }

        n = len(digits)
        ans = []
        def backtrack(ind, path):
            if ind == n:
                ans.append(''.join(path))
                return
            
            for child in t9[digits[ind]]:
                path.append(child)
                backtrack(ind+1, path)
                path.pop()
        
        if not digits:
            return []
        backtrack(0, [])
        return ans