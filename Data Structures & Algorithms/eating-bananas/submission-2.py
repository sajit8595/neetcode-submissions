class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def check(mid):
            reqH = 0
            for p in piles:
                reqH += (p // mid)
                reqH += (1 if p % mid > 0 else 0)
            return reqH <= h 
        
        ans = -1
        while low <= high:
            mid = (low + high) // 2 
            if (check(mid)):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans