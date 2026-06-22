class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1

        # 0, 1, 2, 3
        # 1st ele on even, then 2nd on odd

        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 0:
                mid += 1
            if mid % 2 == 1:
                if nums[mid-1] == nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            # else:
            #     if nums[mid+1] == nums[mid]:
            #         low = mid+2
            #     else:
            #         high = mid-1
        
        return nums[low]