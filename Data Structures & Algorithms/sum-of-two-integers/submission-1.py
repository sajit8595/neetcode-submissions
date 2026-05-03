class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a + b without + or -
        # to force it to 32 bits
        mask = 0xFFFFFFFF
        ans = 0
        rembit = 0
        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1

            newbit = abit ^ bbit ^ rembit
            rembit = (abit & bbit) | (bbit & rembit) | (rembit & abit)
            if newbit:
                ans |= (1 << i)
        
        ans = ans & mask
        return ans if ans <= 0x7FFFFFFF else ~(ans ^ mask)