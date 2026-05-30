"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        allTimes = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            allTimes.append((start, 1))
            allTimes.append((end, -1))
        
        allTimes.sort()

        ans = 0
        currSum = 0
        for time, room in allTimes:
            currSum += room
            ans = max(ans, currSum)
        
        return ans