class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def removeFromSet(val, s, diff):
            ans = 0
            nval = val + diff
            while nval in s:
                s.remove(nval)
                nval += diff
                ans += 1
            return ans

        s = set(nums)
        ans = 0
        for no in nums:
            current = 1 + removeFromSet(no, s, -1) + removeFromSet(no, s, 1)
            ans = max(ans, current)
        return ans
        