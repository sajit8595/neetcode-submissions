class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = [intervals[0]]
        for i in range(1, n):
            s1, e1 = ans[-1]
            s2, e2 = intervals[i]
            if s2 <= e1:
                ans[-1] = [s1, max(e1, e2)]
            else:
                ans.append([s2, e2])
        return ans