from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n= len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0]=1
        for row in range(m):
            for col in range(n):
                if not row and not col:
                    continue

                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = None
                else:
                    up   = obstacleGrid[row-1][col] if 0<row else None
                    left = obstacleGrid[row][col-1] if 0<col else None

                    if up and left:
                        obstacleGrid[row][col] = up+left
                    elif up:
                        obstacleGrid[row][col] = up
                    elif left:
                        obstacleGrid[row][col] = left
                    else:
                        obstacleGrid[row][col] = None
        return obstacleGrid[m-1][n-1] if obstacleGrid[m-1][n-1] else 0

def main():
    obstacleGrid = [[0,1],[1,0]]
    solution = Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid))

if __name__ =="__main__":
    main()