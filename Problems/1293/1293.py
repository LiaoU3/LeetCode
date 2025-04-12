from typing import List
from collections import defaultdict, deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        remain = [[-1] * COL for _ in range(ROW)]
        q = deque([(0, 0, k)])

        res = 0
        while q:
            length = len(q)
            for _ in range(length):
                r, c, k = q.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return res
                for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROW and 0 <= nc < COL:
                        nk = k
                        if grid[nr][nc] == 0:
                            if nk > remain[nr][nc]:
                                remain[nr][nc] = nk
                                q.append((nr, nc, nk))
                        elif grid[nr][nc] == 1 and nk > 0:
                            nk -= 1
                            if nk > remain[nr][nc]:
                                remain[nr][nc] = nk
                                q.append((nr, nc, nk))
            res += 1
        return -1


grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
sol = Solution()
print(sol.shortestPath(grid, k))
