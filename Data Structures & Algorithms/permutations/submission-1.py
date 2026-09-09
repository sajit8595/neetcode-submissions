class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def recur(path, vis):
            if len(path) == n:
                ans.append(path.copy())
                return
            
            for nInd in range(n):
                if vis[nInd] == False:
                    path.append(nums[nInd])
                    vis[nInd] = True
                    recur(path, vis)
                    vis[nInd] = False
                    path.pop()
        
        recur([], [False] * n)
        return ans