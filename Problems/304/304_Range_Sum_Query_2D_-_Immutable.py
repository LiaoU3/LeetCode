from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROW = len(matrix)
        COL = len(matrix[0])
        for r in range(ROW):
            row_sum = 0
            for c in range(COL):
                row_sum += matrix[r][c]
                matrix[r][c] = row_sum + (matrix[r - 1][c] if r - 1 >= 0 else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.matrix[row2][col2]
        top = self.matrix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        left = self.matrix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        top_left = self.matrix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        return total - top - left + top_left


# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         self.pre_sum_matrix = matrix
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 self.pre_sum_matrix[i][j] = self.pre_sum_matrix[i][j] + (self.pre_sum_matrix[i][j-1] if j-1>=0 else 0) + (self.pre_sum_matrix[i-1][j] if i-1>=0 else 0) - (self.pre_sum_matrix[i-1][j-1] if i-1>=0 and j-1>=0 else 0)
#         print(self.pre_sum_matrix)

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         return self.pre_sum_matrix[row2][col2] - (self.pre_sum_matrix[row2][col1-1] if col1-1>=0 else 0) - (self.pre_sum_matrix[row1-1][col2] if row1-1>=0 else 0) + (self.pre_sum_matrix[row1-1][col1-1] if row1-1 >=0 and col1-1>=0 else 0)

# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         total = 0
#         for i in range(row1, row2+1):
#             for j in range(col1, col2+1):
#                 total += self.matrix[i][j]
#         return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)