class Solution:
    def __init__(self):
        self.n = -1

    def numDecodings(self, s: str) -> int:
        self.n = len(s)

        next2 = 1
        next1 = 1 if s[-1] != '0' else 0

        for ind in range(self.n-2, -1, -1):
            ans = 0
            oneStep = int(s[ind])
            if 1 <= oneStep <= 9:
                ans += next1
            twoStep = int(s[ind] + s[ind+1])
            if 10 <= twoStep <= 26:
                ans += next2
            next2 = next1
            next1 = ans
        return next1


        