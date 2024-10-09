class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(board)
        n = len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n):
                return False
            if board[r][c] != word[i]:
                return False
            if (r, c) in used:
                return False
            used.add((r, c))
            for dir_r, dir_c in direction:
                next_r = r + dir_r
                next_c = c + dir_c
                if dfs(next_r, next_c, i + 1):
                    return True
            used.remove((r, c))
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
