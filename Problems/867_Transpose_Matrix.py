from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transposed = [[0 for _ in range(m)] for _ in range(n)] 
        for row in range(m):
            for col in range(n):
                transposed[col][row] = matrix[row][col]
        return transposed

if __name__ =='__main__':
    matrix = [[1,2,3],[4,5,6]]
    sol = Solution()
    print(sol.transpose(matrix))