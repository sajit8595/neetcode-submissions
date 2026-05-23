class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        currAns = 0
        for n in nums:
            if n == 1:
                currAns += 1
            else:
                ans = max(ans, currAns)
                currAns = 0
        return max(ans, currAns)