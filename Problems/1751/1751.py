from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        cache = {}  # key: (index, length), val: total value

        def binary_search(day, l, r):
            if l > r:
                return l
            m = l + (r - l) // 2
            if events[m][0] <= day:
                return binary_search(day, m + 1, r)
            else:
                return binary_search(day, l, m - 1)

        def dfs(i, length):
            if i == len(events):
                return 0
            if length == 0:
                return 0
            if (i, length) in cache:
                return cache[(i, length)]
            take = events[i][2]
            j = binary_search(events[i][1], i + 1, len(events) - 1)
            take += dfs(j, length - 1)
            skip = dfs(i + 1, length)
            cache[(i, length)] = max(take, skip)
            return cache[(i, length)]

        return dfs(0, k)


events = [[1,2,4],[3,4,3],[2,3,10]]
k = 2
sol = Solution()
print(sol.maxValue(events, k))
