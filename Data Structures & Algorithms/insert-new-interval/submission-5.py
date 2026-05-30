class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval

        ans = []
        for ind in range(len(intervals)):
            s, e = intervals[ind]
            if ne < s:
                ans.append([ns, ne])
                ans = ans + intervals[ind:]
                return ans
            elif e < ns:
                ans.append([s, e])
            else:
                ns, ne = min(s, ns), max(e, ne)

        ans.append([ns, ne])
        return ans

        # ns ------ ne
        #     s --------- e

        # s -------- e
        #     ns -------- e
        
        # s --------- e
        #     ns-ne
        
        # ns--------ne
        #     s-e
