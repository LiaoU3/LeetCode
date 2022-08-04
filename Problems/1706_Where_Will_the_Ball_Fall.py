from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        def fall(r, c):
            if r == m:
                return c
            if grid[r][c] == 1:
                if c == n - 1:
                    return -1
                if grid[r][c+1] == -1:
                    return -1
                return fall(r+1, c+1)
            else:
                if c == 0:
                    return -1
                if grid[r][c-1] == 1:
                    return -1
                return fall(r+1, c-1)
        res = []
        for i in range(n):
            res.append(fall(0, i))
        return res

if __name__ == '__main__':
    sol = Solution()
    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    print(sol.findBall(grid))