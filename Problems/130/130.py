from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or r == ROW - 1 or c == 0 or c == COL - 1) and board[r][c] == "O":
                    q.append((r, c))

        # Change "O" to "#" if connected to the edges
        while q:
            r, c = q.popleft()
            board[r][c] = "#"
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == "O":
                    q.append((nr, nc))

        # Change "#" back to "O" and change "O" to "X"
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

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