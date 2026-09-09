class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        ans = []

        def recur(ind, path, curTot):
            if curTot > target:
                return

            if ind == n:
                if curTot == target:
                    ans.append(path[:])
                return
            
            recur(ind+1, path, curTot)

            path.append(nums[ind])
            curTot += nums[ind]
            recur(ind, path, curTot)
            curTot -= nums[ind]
            path.pop()
        
        recur(0, [], 0)

        return ans

