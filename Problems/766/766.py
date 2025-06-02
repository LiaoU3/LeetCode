class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True
