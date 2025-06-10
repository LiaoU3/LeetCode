class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if r == c == 0:
                    continue
                up = grid[r - 1][c] if r - 1 >= 0 else float("Inf")
                left = grid[r][c - 1] if c - 1 >= 0 else float("Inf")
                grid[r][c] += min(up, left)
        return grid[-1][-1]
