class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        seen = set()  # r, c
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not(0 <= r < ROW and 0 <= c < COL):
                return False
            if board[r][c] != word[i]:
                return False
            if (r, c) in seen:
                return False
            seen.add((r, c))
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if dfs(nr, nc, i + 1):
                    return True
            seen.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False