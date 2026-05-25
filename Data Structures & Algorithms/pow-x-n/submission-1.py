class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recur(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            
            half = recur(x, n // 2)
            full = half * half
            
            return full * x if n & 1 else full
        
        ans = recur(abs(x), abs(n))

        if x < 0 and abs(n) & 1:
            ans = -ans

        return 1 / ans if n < 0 else ans