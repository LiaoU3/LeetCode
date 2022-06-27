from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW = len(mat)
        COL = len(mat[0])
        dist = [[0 for c in range(COL)]for r in range(ROW)]
        curr = deque([])
        for r in range(ROW):
            for c in range(COL):
                if mat[r][c]:
                    dist[r][c] = 10**4+1
                else:
                    curr.append((r, c))
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while curr:
            curr_r, curr_c = curr.popleft()
            for dir in directions:
                nxt_r, nxt_c = curr_r + dir[0], curr_c + dir[1]
                if ROW>nxt_r>=0 and COL>nxt_c>=0 and dist[nxt_r][nxt_c]>dist[curr_r][curr_c]+1:
                        dist[nxt_r][nxt_c] = dist[curr_r][curr_c]+1
                        curr.append((nxt_r, nxt_c))
        return dist