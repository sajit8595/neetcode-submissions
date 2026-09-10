class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []
        n = len(intervals)
        for i in range(n):
            s, e = intervals[i]
            ns, ne = newInterval
            if ne < s:
                return ans + [newInterval] + intervals[i:]
            elif e < ns:
                ans.append(intervals[i])
            else:
                ns, ne = min(s, ns), max(e, ne)
                newInterval = [ns, ne]

        ans.append(newInterval)
        return ans