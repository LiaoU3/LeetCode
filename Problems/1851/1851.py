from typing import List
from heapq import heappush, heappop


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = [(num, i) for i, num in enumerate(queries)]
        q.sort()

        intervals.sort()

        j = 0
        hp = []  # (length of the interval, right index of the interval)
        res = [-1] * len(q)

        for num, i in q:
            while j < len(intervals) and intervals[j][0] <= num:
                heappush(hp, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                j += 1
            while hp and hp[0][1] < num:
                heappop(hp)
            if hp:
                res[i] = hp[0][0]
        return res

sol = Solution()
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
print(sol.minInterval(intervals, queries))