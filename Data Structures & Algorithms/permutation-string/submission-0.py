class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1d = {}
        s2d = {}
        n1 = len(s1)

        for s in s1:
            s1d[s] = s1d.get(s, 0) + 1

        def check(a, b):
            print(s1d, s2d)
            for k in a:
                if k not in b or a[k] != b[k]:
                    return False
            return True

        curr = 0
        i = 0
        for s in s2:
            s2d[s] = s2d.get(s, 0) + 1
            curr += 1
            if curr == n1:
                if check(s1d, s2d):
                    return True
                else:
                    s2d[s2[i]] -= 1
                    curr -= 1
                    i += 1
        return False