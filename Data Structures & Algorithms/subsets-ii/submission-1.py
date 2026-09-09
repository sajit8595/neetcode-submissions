class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        n = len(nums)

        def recur(ind, path):
            ans.append(path.copy())
            
            for nInd in range(ind, n):
                if nInd > ind and nums[nInd-1] == nums[nInd]:
                    continue
                    
                path.append(nums[nInd])
                recur(nInd+1, path)
                path.pop()
        
        recur(0, [])
        return ans