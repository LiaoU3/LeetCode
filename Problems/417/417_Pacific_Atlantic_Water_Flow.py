from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)  # the number of rows
        N = len(heights[0])  # the number of cols
        to_pac = [[False for _ in range(N)] for _ in range(M)]
        to_atl = [[False for _ in range(N)] for _ in range(M)]

        def in_bound(r, c):
            if 0 <= r < M and 0 <= c < N:
                return True
            else:
                return False

        def dfs(r, c, ocean):
            ocean[r][c] = True
            for dir_r, dir_c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_r = r + dir_r
                next_c = c + dir_c
                if in_bound(next_r, next_c) and not ocean[next_r][next_c] and heights[r][c] <= heights[next_r][next_c]:
                    dfs(next_r, next_c, ocean)
        
        for r in range(M):
            dfs(r, 0, to_pac)
            dfs(r, N - 1, to_atl)
        for c in range(N):
            dfs(0, c, to_pac)
            dfs(M - 1, c, to_atl)
        
        res = []
        for r in range(M):
            for c in range(N):
                if to_pac[r][c] and to_atl[r][c]:
                    res.append([r, c])
        return res

# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         m = len(heights)
#         n = len(heights[0])
#         pac = [[0 for i in range(n)] for j in range(m)]
#         atl = [[0 for i in range(n)] for j in range(m)]
#         qu = deque([])
#         for i in range(n):
#             pac[0][i] = 1
#             qu.append((0, i))
#         for i in range(1, m):
#             pac[i][0] = 1
#             qu.append((i, 0))
#         directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
#         while(qu):
#             r, c = qu.popleft()
#             for dr, dc in directions:
#                 nextr = r + dr
#                 nextc = c + dc
#                 if m > nextr >= 0 and n > nextc >= 0 and not pac[nextr][nextc] and heights[r][c] <= heights[nextr][nextc]:
#                     pac[nextr][nextc] = 1
#                     qu.append((nextr, nextc))
    
#         qu = deque([]) 
#         for i in range(n):
#             atl[m-1][i] = 1
#             qu.append((m-1, i))
        
#         for i in range(m-1):
#             atl[i][n-1] = 1
#             qu.append((i, n-1))
    
#         while(qu):
#             r, c = qu.popleft()
#             for dr, dc in directions:
#                 nextr = r + dr
#                 nextc = c + dc
#                 if m > nextr >= 0 and n > nextc >= 0 and not atl[nextr][nextc] and heights[r][c] <= heights[nextr][nextc]:
#                     atl[nextr][nextc] = 1
#                     qu.append((nextr, nextc))
#         res = []
#         for i in range(m):
#             for j in range(n):
#                 if pac[i][j] and atl[i][j]:
#                     res.append([i, j])
#         return res