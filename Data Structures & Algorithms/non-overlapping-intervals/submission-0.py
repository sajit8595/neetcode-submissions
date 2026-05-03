class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = [intervals[0]]
        remove = 0
        for i in range(1, len(intervals)):
            s1, e1 = ans[-1]
            s2, e2 = intervals[i]
            if s2 < e1:
                if e2 < e1:
                    ans[-1] = intervals[i]
                remove += 1
            else:
                ans.append(intervals[i])
        return remove