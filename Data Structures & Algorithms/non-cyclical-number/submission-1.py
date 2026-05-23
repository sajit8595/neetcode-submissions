class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquareSum(n):
            ans = 0
            while n:
                rem = n % 10
                ans += (rem ** 2)
                n = n // 10
            return ans
        
        # vis = set()
        # while n not in vis:
        #     vis.add(n)
        #     n = getSquareSum(n)
        #     if n == 1:
        #         return True
        # return False

        slow = n
        fast = getSquareSum(n)

        while slow != fast:
            slow = getSquareSum(slow)
            fast = getSquareSum(getSquareSum(fast))
        return slow == 1
