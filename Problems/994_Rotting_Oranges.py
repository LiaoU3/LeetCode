from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        rottens = deque([])
        fresh_cnt = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    rottens.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        if fresh_cnt == 0:
            return 0

        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        cnt = 0
        while rottens:
            cnt += 1
            len_q = len(rottens)
            for _ in range(len_q):
                r, c = rottens.popleft()
                for dir in directions:
                    next_r = r+dir[0]
                    next_c = c+dir[1]
                    if ROW>next_r>=0 and COL>next_c>=0 and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2
                        rottens.append((next_r, next_c))
                        fresh_cnt -= 1
        
        return -1 if fresh_cnt else cnt-1

if __name__ =='__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    sol = Solution()
    print(sol.orangesRotting(grid))