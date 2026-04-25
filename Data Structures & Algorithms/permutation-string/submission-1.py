class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        s1a = [0] * 26
        s2a = [0] * 26

        def getAscii(ch):
            return ord(ch) - ord('a')

        for i in range(n1):
            s1a[getAscii(s1[i])] += 1
            s2a[getAscii(s2[i])] += 1
        
        equal = 0
        for i in range(26):
            if s1a[i] == s2a[i]:
                equal += 1

        if equal == 26:
            return True
        
        l = 0
        for r in range(n1, n2):
            lAscii = getAscii(s2[l])
            rAscii = getAscii(s2[r])

            if s1a[lAscii] == s2a[lAscii]:
                equal -= 1
            if s1a[rAscii] == s2a[rAscii]:
                equal -= 1

            s2a[lAscii] -= 1
            s2a[rAscii] += 1

            if s1a[lAscii] == s2a[lAscii]:
                equal += 1
            if s1a[rAscii] == s2a[rAscii]:
                equal += 1
            
            if equal == 26:
                return True

            l += 1
        
        return False
