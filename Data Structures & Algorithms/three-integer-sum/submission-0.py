class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for k in range(n):
            i = k+1; j = n-1
            while i < j:
                sumij = nums[i] + nums[j]
                if sumij + nums[k] == 0:
                    ans.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif sumij + nums[k] < 0:
                    i += 1
                else:
                    j -= 1
        return list(ans)
