from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def binary_search(l, r):
            if l > r:
                return l
            m = (l + r) // 2
            if intervals[m][0] == newInterval[0]:
                return m
            elif intervals[m][0] > newInterval[0]:
                return binary_search(l, m - 1)
            else:
                return binary_search(m + 1, r)
        
        i = binary_search(0, len(intervals) - 1)
        intervals.insert(i, newInterval)

        res = []
        for j in range(max(i - 1, 0), len(intervals)):
            if not res or res[-1][1] < intervals[j][0]:
                res.append(intervals[j])
            else:
                res[-1][1] = max(res[-1][1], intervals[j][1])
        return res

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

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

newInterval = [4,8]
s = Solution()
print(s.insert(intervals, newInterval))