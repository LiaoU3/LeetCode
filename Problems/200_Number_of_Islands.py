# bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ROW = len(grid)
        COL = len(grid[0])
        cnt = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]=='1':
                    qu = deque([(r, c)])
                    grid[r][c] = '0'
                    cnt += 1
                    while qu:
                        cr, cc = qu.pop()
                        for dr, dc in directions:
                            nr, nc = cr+dr, cc+dc
                            if ROW>nr>=0 and COL>nc>=0 and grid[nr][nc]=='1':
                                grid[nr][nc] = 0
                                qu.append((nr, nc))
        return cnt

# dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ROW = len(grid)
        COL = len(grid[0])
        
        def dfs(r, c):
            if not (ROW>r>=0 and COL>c>=0 and grid[r][c] == '1'):
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        cnt = 0 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(r, c)
        return cnt