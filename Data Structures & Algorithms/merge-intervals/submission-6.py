class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            s1, e1 = ans.pop()
            s2, e2 = intervals[i]

            if e1 < s2:
                ans.append([s1, e1])
                ans.append([s2, e2])
            else:
                minS, maxE = min(s1, s2), max(e1, e2)
                ans.append([minS, maxE])
        
        return ans