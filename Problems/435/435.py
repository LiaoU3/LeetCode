# Cleaener and faster solution
# O(n*log(n))
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = -float("Inf")
        res = 0
        for start, end in intervals:
            if start < prev:
                prev = min(prev, end)
                res += 1
            else:
                prev = end
        return res

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        new_intervals = [[-float("Inf"), -float("Inf")]]
        cnt = 0
        for start, end in intervals:
            pre_end = new_intervals[-1][1]
            # If it is not overlapped with the previous interval
            if start >= pre_end:
                new_intervals.append([start, end])
            # If it is overlapped with the previous interval
            else:
                if pre_end > end:
                    new_intervals.pop()
                    new_intervals.append([start, end])
                cnt += 1
        return cnt