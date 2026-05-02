class Solution:
    def hammingWeight(self, n: int) -> int:
        # solve by count of 1's by 1 bit i.e >> i.e // 2
        ans1 = 0
        nn = n
        while nn:
            if nn & 1:
                ans1 += 1
            nn = (nn >> 1)

        # solve by directly going to next set bit
        ans2 = 0
        nn = n
        # Performing n & (n - 1) removes the rightmost 1 bit from n
        while nn:
            ans2 += 1
            nn = nn & (nn-1)
        
        if ans1 == ans2:
            return ans1