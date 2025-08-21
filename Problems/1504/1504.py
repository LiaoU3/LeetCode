class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ROW = len(mat)
        COL = len(mat[0])
        rows = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        for r in range(ROW):
            for c in range(COL):
                rows[r + 1][c + 1] = mat[r][c]
        res = 0
        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                if rows[r][c] == 0:
                    continue
                rows[r][c] += rows[r][c - 1]
                res += rows[r][c]
                min_val = rows[r][c]
                for r_ in range(r - 1, -1, -1):
                    min_val = min(min_val, rows[r_][c])
                    res += min_val
        return res
