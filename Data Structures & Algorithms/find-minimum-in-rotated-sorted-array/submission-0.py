class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        l = 0; r = len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                if nums[l] < ans:
                    ans = nums[l]
                l = mid+1
            else:
                r = mid
        return ans