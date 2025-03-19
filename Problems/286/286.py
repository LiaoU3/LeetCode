class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        rnd = 0
        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = rnd + 1
                        q.append((nr, nc))
            rnd += 1

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        q = deque()  # (row, col, distance)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        if len(q) == 0:
            return

        while q:
            r, c, d = q.popleft()
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr = r + dr
                nc = c + dc
                # If on the board and not been traversed
                if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))
