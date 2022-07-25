from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac = [[0 for i in range(n)] for j in range(m)]
        atl = [[0 for i in range(n)] for j in range(m)]
        qu = deque([])
        for i in range(n):
            pac[0][i] = 1
            qu.append((0, i))
        for i in range(1, m):
            pac[i][0] = 1
            qu.append((i, 0))
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while(qu):
            r, c = qu.popleft()
            for dr, dc in directions:
                nextr = r + dr
                nextc = c + dc
                if m > nextr >= 0 and n > nextc >= 0 and not pac[nextr][nextc] and heights[r][c] <= heights[nextr][nextc]:
                    pac[nextr][nextc] = 1
                    qu.append((nextr, nextc))
    
        qu = deque([]) 
        for i in range(n):
            atl[m-1][i] = 1
            qu.append((m-1, i))
        
        for i in range(m-1):
            atl[i][n-1] = 1
            qu.append((i, n-1))
    
        while(qu):
            r, c = qu.popleft()
            for dr, dc in directions:
                nextr = r + dr
                nextc = c + dc
                if m > nextr >= 0 and n > nextc >= 0 and not atl[nextr][nextc] and heights[r][c] <= heights[nextr][nextc]:
                    atl[nextr][nextc] = 1
                    qu.append((nextr, nextc))
        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res