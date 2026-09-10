class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        minVal = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                minVal = min(minVal, nums[low])
                low = mid+1
            else:
                minVal = min(minVal, nums[mid])
                high = mid-1

        return minVal