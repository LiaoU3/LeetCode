"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        pre_end = -1
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < pre_end:
                return False
            pre_end = end
        return True