from typing import List
from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        hp = [(grid[0][0], 0, 0)]  # time, row, col
        seen = set([(0, 0)])
        while hp:
            time, r, c = heappop(hp)
            if r == c == N - 1:
                return time
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen:
                    heappush(hp,(max(grid[nr][nc], time), nr, nc))
                    seen.add((nr, nc))

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
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(sol.swimInWater(grid))