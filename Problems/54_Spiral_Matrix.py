from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(matrix)
        n = len(matrix[0])
        currDir = 0
        count = 0
        r, c = 0, -1
        
        res = []
        while count != m*n:
            dr, dc = directions[currDir]
            nextr, nextc = r + dr, c + dc
            if m > nextr >= 0 and n > nextc >= 0 and matrix[nextr][nextc] != -101:
                res.append(matrix[nextr][nextc])
                matrix[nextr][nextc] = -101
                r, c = nextr, nextc
                count += 1
            else:
                currDir += 1
                currDir %= 4
        return res

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix))