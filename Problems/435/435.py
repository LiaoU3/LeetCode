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