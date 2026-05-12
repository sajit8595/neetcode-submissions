"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        khatam = []
        for interval in intervals:
            s, e = interval.start, interval.end
            if khatam and khatam[0] <= s:
                heapq.heappop(khatam)
            heapq.heappush(khatam, e)
        # print(khatam)
        return len(khatam)