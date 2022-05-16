from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        if len(grid) == 1:
            return 1
        curr_position = [(0, 0)]
        grid[0][0] = 1
        direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        count = 1
        while curr_position:
            count += 1
            next_position = []
            for x, y in curr_position:
                for dx, dy in direction:
                    x_next = x+dx
                    y_next = y+dy
                    if 0 <= x_next < N and 0 <= y_next < N and grid[x_next][y_next] == 0:
                        if x_next == y_next == N-1:
                            return count
                        next_position.append((x_next, y_next))
                        grid[x_next][y_next] = 1
            curr_position = next_position
        return -1

def main():
    grid = [[0]]
    solution = Solution()
    print(solution.shortestPathBinaryMatrix(grid))

if __name__ == "__main__":
    main()