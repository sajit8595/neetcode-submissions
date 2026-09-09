class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)

        def recur(ind, path):
            ans.append(path.copy())
            
            for nInd in range(ind, n):
                path.append(nums[nInd])
                recur(nInd+1, path)
                path.pop()
        
        recur(0, [])
        return ans