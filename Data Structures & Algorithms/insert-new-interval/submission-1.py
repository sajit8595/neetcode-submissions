class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        isInserted = False
        for s, e in intervals:
            if newInterval[0] < s:
                newIntervals.append(newInterval)
                isInserted = True
            newIntervals.append((s, e))
        if isInserted == False:
            newIntervals.append(newInterval)
        
        intervals = newIntervals

        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            s1, e1 = ans[-1]
            s2, e2 = intervals[i]
            if s2 <= e1:
                ans[-1] = [s1, max(e1, e2)]
            else:
                ans.append([s2, e2])
        return ans
