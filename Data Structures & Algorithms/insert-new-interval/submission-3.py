class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            s1, e1 = ans[-1]
            s2, e2 = intervals[i]
            if s2 <= e1:
                ans[-1] = [s1, max(e1, e2)]
            else:
                ans.append([s2, e2])
        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            s1, e1 = intervals[i]
            s2, e2 = newInterval
            if s2 > e1:
                ans.append(intervals[i])
            elif e2 < s1:
                ans.append(newInterval)
                return ans + intervals[i:]
            else:
                newInterval = [min(s1, s2), max(e1, e2)]
        ans.append(newInterval)
        return ans

        
