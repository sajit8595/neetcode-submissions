class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def recur(i, path):
            if i >= n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                if isPalin(i, j):
                    path.append(s[i:j+1])
                    recur(j+1, path)
                    path.pop()
        
        def isPalin(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        recur(0, [])
        return ans
