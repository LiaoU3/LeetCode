from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0  # included
        right = len(matrix[0])  # not included
        up = 0  # included
        down = len(matrix)  # not included
        while left < right and up < down:
            print(left, right, up, down)
            # right
            for c in range(left, right):
                res.append(matrix[up][c])
            up += 1
            # down
            for r in range(up, down):
                res.append(matrix[r][right - 1] )
            right -= 1
            if not (left < right and up < down):
                break
            # left
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[down - 1][c])
            down -= 1
            # up
            for r in range(down - 1, up - 1, -1):
                res.append(matrix[r][left])
            left += 1
        return res

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
#         m = len(matrix)
#         n = len(matrix[0])
#         currDir = 0
#         count = 0
#         r, c = 0, -1
        
#         res = []
#         while count != m*n:
#             dr, dc = directions[currDir]
#             nextr, nextc = r + dr, c + dc
#             if m > nextr >= 0 and n > nextc >= 0 and matrix[nextr][nextc] != -101:
#                 res.append(matrix[nextr][nextc])
#                 matrix[nextr][nextc] = -101
#                 r, c = nextr, nextc
#                 count += 1
#             else:
#                 currDir += 1
#                 currDir %= 4
#         return res

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix))