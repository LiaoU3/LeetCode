from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        not_surrounded = set()
        visited = set()
        def dfs(r, c):
            if not 0 <= r < ROW:
                return False
            if not 0 <= c < COL:
                return False
            if (r, c) in visited:
                return True
            if (r, c) in not_surrounded:
                return False
            if board[r][c] == "X":
                return True
            visited.add((r, c))
            res = True
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr = r + dr
                nc = c + dc
                res = res and dfs(nr, nc)
            return res
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "X":
                    continue
                visited = set()
                if dfs(r, c):
                    for r_, c_ in visited:
                        board[r_][c_] = "X"
                else:
                    not_surrounded |= visited

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

sol = Solution()
sol.solve(board)
print(board)