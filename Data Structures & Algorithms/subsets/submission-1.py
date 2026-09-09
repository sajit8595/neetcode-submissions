class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)

        def recur(ind, path):
            if ind == n:
                ans.append(path[:])
                return
            
            recur(ind+1, path)

            path.append(nums[ind])
            recur(ind+1, path)
            path.pop()
        
        recur(0, [])
        return ans