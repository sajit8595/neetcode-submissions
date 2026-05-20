class Solution:
    def __init__(self):
        self.s1 = ''
        self.s2 = ''
        self.s3 = ''

        self.s1Len = 0
        self.s2Len = 0
        self.s3Len = 0

        self.memo = {}

    def recursion(self, ind1, ind2):
        ind3 = (ind1 + ind2)
        if ind3 == self.s3Len:
            return ind1 == self.s1Len and ind2 == self.s2Len
        
        key = (ind1, ind2)
        if key in self.memo:
            return self.memo[key]

        if ind1 < self.s1Len and self.s1[ind1] == self.s3[ind3]:
            recurInd1 = self.recursion(ind1+1, ind2)
            if recurInd1:
                self.memo[key] = True
                return self.memo[key]
        
        if ind2 < self.s2Len and self.s2[ind2] == self.s3[ind3]:
            recurInd2 = self.recursion(ind1, ind2+1)
            if recurInd2:
                self.memo[key] = True
                return self.memo[key]

        self.memo[key] = False
        return self.memo[key]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
        self.s1Len = len(s1)
        self.s2Len = len(s2)
        self.s3Len = len(s3)

        if (self.s1Len + self.s2Len) != self.s3Len:
            return False

        return self.recursion(0, 0)