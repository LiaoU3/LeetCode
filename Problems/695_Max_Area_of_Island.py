from typing import List
from collections import deque

# bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.curr_area = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        ROW = len(grid)
        COL = len(grid[0])

        def bfs(r, c):
            if grid[r][c]==0:
                return
            grid[r][c] = 0
            self.curr_area += 1
            que = deque([[r,c]])
            while que:
                curr_r, curr_c = que.pop()
                for dir in directions:
                    dr, dc = dir
                    nxt_r = curr_r + dr
                    nxt_c = curr_c + dc
                    if ROW>nxt_r>=0 and COL>nxt_c>=0 and grid[nxt_r][nxt_c]:
                        que.append([nxt_r, nxt_c])
                        grid[nxt_r][nxt_c] = 0
                        self.curr_area += 1

        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                self.curr_area = 0
                bfs(r, c)
                max_area = max(max_area, self.curr_area)
        return max_area

# dfs without self
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        def dfs(r, c):
            if not(ROW>r>=0 and COL>c>=0)or not grid[r][c]:
                return 0
            grid[r][c] = 0
            total = 1
            for dir in directions:
                nr = r+dir[0]
                nc = c+dir[1]
                total += dfs(nr, nc)
            return total
        maxArea = 0
        for r in range(ROW):
            for c in range(COL):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea

# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.curr_area = 0
        ROW = len(grid)
        COL = len(grid[0])
        def dfs(r, c):
            if grid[r][c]:
                grid[r][c] = 0
                self.curr_area += 1
                if r-1>=0:
                    dfs(r-1, c)
                if ROW>r+1:
                    dfs(r+1, c)
                if c-1>=0:
                    dfs(r, c-1)
                if COL>c+1:
                    dfs(r, c+1)
        max_island = 0
        for r in range(ROW):
            for c in range(COL):
                self.curr_area = 0
                dfs(r, c)
                max_island = max(max_island, self.curr_area)
        return max_island