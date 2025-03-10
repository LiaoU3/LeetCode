"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        days = [0]

        for interval in intervals:
            start = interval.start
            end = interval.end
            time = days[0]
            if time <= start:
                heappop(days)
            heappush(days, end)
                
        return len(days)

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        days = [-1]
        new_intervals = []
        for interval in intervals:
            new_intervals.append([interval.start, interval.end])
        new_intervals.sort()
        for start, end in new_intervals:
            for i, day in enumerate(days):
                if day <= start:
                    days[i] = end
                    break
            else:
                days.append(end)
        return len(days)