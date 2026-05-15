class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k-1:
                if dq[0] <= (i - k):
                    dq.popleft()
                ans.append(nums[dq[0]])
        
        return ans