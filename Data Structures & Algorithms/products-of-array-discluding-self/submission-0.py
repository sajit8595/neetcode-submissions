class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for i in range(n+1)]
        suffix = [1 for i in range(n+1)]

        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(n, 0, -1):
            suffix[i-1] = suffix[i] * nums[i-1]
        
        print(prefix, suffix)
        ans = []
        for i in range(n):
            pref = prefix[i]
            suff = suffix[i+1]
            ans.append(pref * suff)
        
        return ans