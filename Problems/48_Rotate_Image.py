from typing import List

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