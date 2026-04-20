class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for i in range(n+1)]
        suffix = [1 for i in range(n+1)]

        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        ans = []
        for i in range(n):
            pref = prefix[i]
            suff = suffix[i+1]
            ans.append(pref * suff)
        
        return ans