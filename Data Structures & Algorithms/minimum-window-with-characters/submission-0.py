class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ls = len(s)
        lt = len(t)

        ds = {}
        dt = {}
        
        for c in t:
            dt[c] = dt.get(c, 0) + 1
        
        def check(ds, dt):
            for key in dt:
                if key not in ds or ds[key] < dt[key]:
                    return False
            return True

        ans = ''
        ansLen = float('inf')

        l = r = 0
        while r < ls:
            ds[s[r]] = ds.get(s[r], 0) + 1
            while check(ds, dt):
                print(r, ds, dt)
                newLen = r - l + 1
                if newLen < ansLen:
                    ansLen = newLen
                    ans = s[l:r+1]
                ds[s[l]] -= 1
                l += 1
            r += 1
        
        return ans