class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = [intervals[0]]
        remove = 0
        for i in range(1, len(intervals)):
            s1, e1 = ans[-1]
            s2, e2 = intervals[i]
            # over-lapping - pop out previous interval
            if s2 < e1:
                ans.pop()
                remove += 1
                # choose smallest ending point interval
                if e1 < e2:
                    ans.append((s1, e1))
                else:
                    ans.append((s2, e2))
            else:
                ans.append((s2, e2))
        return remove