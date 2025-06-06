class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])
        rows = set()
        cols = set()
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(ROW):
            for c in range(COL):
                if r in rows or c in cols:
                    matrix[r][c] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        ROW = len(matrix)
        COL = len(matrix[0])
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in rows:
            for c in range(COL):
                matrix[r][c] = 0

        for r in range(ROW):
            for c in cols:
                matrix[r][c] = 0