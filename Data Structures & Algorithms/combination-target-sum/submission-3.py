class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        ans = []

        def recur(ind, path, curTot):
            if curTot == target:
                ans.append(path[:])
                return

            for nInd in range(ind, n):
                if curTot + nums[nInd] > target:
                    return

                path.append(nums[nInd])
                curTot += nums[nInd]
                recur(nInd, path, curTot)
                curTot -= nums[nInd]
                path.pop()
            
        recur(0, [], 0)

        return ans

