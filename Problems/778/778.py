from typing import List
from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)]  # num, r, c
        time = 0
        visited = set([grid[0][0]])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        for time in range(len(grid) ** 2):
            while h and h[0][0] <= time:
                num, r, c = heappop(h)
                if r == c == len(grid) - 1:
                    return time
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid)):
                        continue
                    num = grid[nr][nc]
                    if num in visited:
                        continue
                    visited.add(num)
                    heappush(h, (num, nr, nc))


sol = Solution()
grid = [[0,2],[1,3]]
print(sol.swimInWater(grid))