class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        def recur(ind, path, currSum):
            if currSum == target:
                ans.append(path[:])
                return

            if ind == n:
                return
                
            if currSum + nums[ind] <= target:
                path.append(nums[ind])
                recur(ind, path, currSum + nums[ind])
                path.pop()
            recur(ind+1, path, currSum)
        
        recur(0, [], 0)
        return ans
