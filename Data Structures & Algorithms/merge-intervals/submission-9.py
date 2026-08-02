class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans = []
        ans.append(intervals[0])
        n = len(intervals)
        for i in range(1, n):
            ps, pe = ans[-1]
            ns, ne = intervals[i]
            if ns <= pe:
                ans[-1][1] = max(pe, ne)
            else:
                ans.append([ns, ne])
        return ans