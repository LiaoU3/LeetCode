"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_ls = [[-1, -1]]
        for interval in intervals:
            intervals_ls.append([interval.start, interval.end])

        intervals_ls.sort()

        for i in range(1, len(intervals_ls)):
            if intervals_ls[i][0] < intervals_ls[i - 1][1]:
                return False

        return True
