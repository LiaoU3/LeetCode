from typing import List


# DFS with dp to store the previous best value
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)  # rows
        n = len(matrix[0])  # cols
        dp = [[0 for _ in range(n)] for _ in range(m)]  # 0 stands for not visited
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(r, c):
            if dp[r][c]:  # previous best result
                return dp[r][c]
            best = 0
            for dir_r, dir_c in directions:
                next_r = r + dir_r
                next_c = c + dir_c
                if 0 <= next_r < m and 0 <= next_c < n and matrix[r][c] < matrix[next_r][next_c]:
                    best = max(best, dfs(next_r, next_c))
            dp[r][c] = best + 1
            return dp[r][c]
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res


# DFS with hashmap
# use a map to store the coordinate to longest length could save a lot of calculating time
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         m = len(matrix)
#         n = len(matrix[0])
#         directions = [(-1, 0), (0, 1),  (1, 0),  (0, -1)]
#         map_of_coord_to_length = {}

#         def dfs(x ,y):
#             if (x, y) in map_of_coord_to_length:
#                 return map_of_coord_to_length[(x, y)]
#             max_length = 1
#             for dx, dy in directions:
#                 x_next = x+dx
#                 y_next = y+dy
#                 if 0<=x_next<m and 0<=y_next<n and matrix[x][y]<matrix[x_next][y_next]:
#                     max_length = max(max_length, dfs(x_next, y_next) + 1)
#             map_of_coord_to_length[(x, y)] = max_length
#             return max_length

#         max_length = 1
#         for x in range(m):
#             for y in range(n):
#                 max_length = max(max_length, dfs(x, y))
#         return max_length

# BFS
# It will get TLE wintout a hashmap
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         m = len(matrix)
#         n = len(matrix[0])
#         currents = [(x, y) for x in range(m) for y in range(n)]
#         directions = [(-1, 0), (0, 1),  (1, 0),  (0, -1)]
#         cnt = 0
#         while currents:
#             cnt += 1
#             nexts = []
#             for x, y in currents:
#                 for dx, dy in directions:
#                     x_new = x+dx
#                     y_new = y+dy
#                     if 0<=x_new<m and 0<=y_new<n and matrix[x][y]<matrix[x_new][y_new]:
#                         nexts.append((x_new, y_new))
#             currents = nexts
#         return cnt

def main():
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    solution = Solution()
    print(solution.longestIncreasingPath(matrix))

if __name__ =='__main__':
    main()