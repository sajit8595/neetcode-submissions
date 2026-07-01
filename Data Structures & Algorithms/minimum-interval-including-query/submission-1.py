class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        intervals.sort(key = lambda x: (x[1]-x[0]))

        # queries = [(queries[i], i) for i in range(len(queries))]
        # queries.sort()

        ans = [-1] * len(queries)

        # i = 0
        for i in range(len(queries)):
            for u, v in intervals:
                if u <= queries[i] <= v:
                    ans[i] = v - u + 1
                    break
            # while i < n and intervals[i][0] < q[0]:
            #     i += 1
            # if i < n and (intervals[i][0] <= q[0] <= intervals[i][1]):
            #     ans[q[1]] = intervals[i][1] - intervals[i][0] + 1
        
        return ans