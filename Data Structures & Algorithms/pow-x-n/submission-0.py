class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recur(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            
            half = recur(x, n // 2)
            
            full = half * half
            if n & 1:
                return full * x
            return full
        
        if x < 0:
            ans = recur(abs(x), abs(n))
            if n < 0:
                ans = 1 / ans
            if abs(n) & 1:
                return -ans
            return ans

        ans = recur(abs(x), abs(n))
        if n < 0:
            return 1 / ans
        return ans