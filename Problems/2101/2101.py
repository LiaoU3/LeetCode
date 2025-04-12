from typing import List
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        adjs = defaultdict(list)  # key: index, val: [i1, i2, i3 ...]
        for i, (x, y, r) in enumerate(bombs):
            for j in range(i):
                x2, y2, r2 = bombs[j]
                distance = (x - x2) ** 2 + (y - y2) ** 2
                if distance <= r ** 2:
                    adjs[i].append(j)
                if distance <= r2 ** 2:
                    adjs[j].append(i)

        seen = set()
        def dfs(u):
            if u in seen:
                return 0
            seen.add(u)
            tmp = 1
            for v in adjs[u]:
                tmp += dfs(v)
            return tmp

        total_seen = set()
        res = 0
        for i in range(len(bombs)):
            if i not in total_seen:
                seen = set()
                res = max(res, dfs(i))
                total_seen |= seen
        return res

bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
sol = Solution()
print(sol.maximumDetonation(bombs))