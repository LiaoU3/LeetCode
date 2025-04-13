class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROW = len(board)
        COL = len(board[0])

        def dfs(r, c):
            board[r][c] = "."
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == "X":
                    dfs(nr, nc)
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "X":
                    res += 1
                    dfs(r, c)
        
        return res
