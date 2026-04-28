class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0; high = len(nums)-1
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            # more optimization; if low < mid < high -> low < high -> array is sorted
            # no need to look left & right halves
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid-1
        return ans