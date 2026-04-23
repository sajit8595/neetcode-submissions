class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = list()
        for k in range(n):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k+1; j = n-1
            while i < j:
                sumij = nums[i] + nums[j]
                if sumij + nums[k] == 0:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif sumij + nums[k] < 0:
                    i += 1
                else:
                    j -= 1
        return ans
