from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse
        for r in range(n):
            for c in range(n // 2):
                # Python way
                matrix[r][c], matrix[r][n - 1 - c] = matrix[r][n - 1 - c], matrix[r][c]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        
        for i in range(m-1):
            for j in range(m-i-1):
                matrix[i][j], matrix[m-j-1][m-i-1] = matrix[m-j-1][m-i-1],  matrix[i][j]
        for i in range(m//2):
            for j in range(m):
                matrix[i][j], matrix[m-i-1][j] = matrix[m-i-1][j], matrix[i][j]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        
        for i in range((m+1) // 2):
            for j in range(m // 2):
                matrix[i][j], matrix[m-1-j][i], matrix[m-1-i][m-1-j], matrix[j][m-1-i] = matrix[m-1-j][i], matrix[m-1-i][m-1-j], matrix[j][m-1-i], matrix[i][j]

if __name__ == '__main__':
    sol = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix)
    print(matrix)