class Solution:
    def reverse(self, x: int) -> int:
        minL = -(1 << 31)
        maxL = (1 << 31) - 1

        isNeg = True if x < 0 else False
        x = -x if isNeg else x

        revX = 0
        count
        while x > 0:
            rem = x % 10
            x = x // 10

            revX = revX * 10
            revX = revX + rem

        ans = -revX if isNeg else revX
        if minL <= ans <= maxL:
            return ans
        return 0