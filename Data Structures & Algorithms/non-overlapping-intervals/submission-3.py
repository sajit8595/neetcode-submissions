class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans = [intervals[0]]
        remove = 0
        for i in range(1, len(intervals)):
            s1, e1 = ans[-1]
            s2, e2 = intervals[i]
            # over-lapping - pop out previous interval or minimize the end
            # choose smallest ending point interval
            # in merging, we use <= and max(e1, e2)
            if s2 < e1:
                remove += 1
                ans[-1] = [s1, min(e1, e2)]
            else:
                ans.append([s2, e2])
        return remove