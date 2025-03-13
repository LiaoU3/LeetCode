from typing import List
from collections import Counter
from heapq import heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = [0]*26
        for c in tasks:
            table[ord(c) - ord('A')] += 1

        maxCnt = max(table)
        maxCntTaskCnt = 0
        for cnt in table:
            if cnt == maxCnt:
                maxCntTaskCnt += 1
        return max((n+1) * (maxCnt-1) + maxCntTaskCnt, len(tasks))


sol = Solution()
tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
print(sol.leastInterval(tasks, 2))