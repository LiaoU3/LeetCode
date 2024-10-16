from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [[-1, -1]]
        is_done = False
        for i, (start, end) in enumerate(intervals):
            # The correct index to insert newIntervals
            if not is_done and start > newInterval[0]:
                # If overlap with the previous one
                if newInterval[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], newInterval[1])
                # If not overlap with the previous one
                else:
                    res.append(newInterval)
                is_done = True
            if start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        # Do the check again in the end
        if not is_done:
            # If overlap with the previous one
            if newInterval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], newInterval[1])
            # If not overlap with the previous one
            else:
                res.append(newInterval)
        return res[1:]

intervals = []

newInterval = [2,3]
s = Solution()
print(s.insert(intervals, newInterval))