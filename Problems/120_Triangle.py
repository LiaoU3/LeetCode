from typing import List

# buttom up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

# top down
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         pre_row = triangle[0]
#         for i in range(1, len(triangle)):
#             triangle[i][0] += pre_row[0]
#             for j in range(1, len(triangle[i])-1):
#                 if pre_row[j] < pre_row[j-1]:
#                     triangle[i][j] += pre_row[j]
#                 else:
#                     triangle[i][j] += pre_row[j-1]
#             triangle[i][-1] += pre_row[-1]
#             pre_row = triangle[i]
#         return min(triangle[-1])

if __name__ == '__main__':
    sol = Solution()
    tri = [[-1],[2,3],[1,-1,-3]]
    print(sol.minimumTotal(tri))