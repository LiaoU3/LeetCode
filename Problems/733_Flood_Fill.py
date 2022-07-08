from collections import deque
from typing import List



# dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        m = len(image)
        n = len(image[0])
        def dfs(row, col):
            if image[row][col] == original_color:
                image[row][col] = color
                if row-1>=0:
                    dfs(row-1, col)
                if m>row+1:
                    dfs(row+1, col)
                if col-1>=0:
                    dfs(row, col-1)
                if n>col+1:
                    dfs(row, col+1)
        dfs(sr, sc)
        return image

# dfs but cleaner
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originColor = image[sr][sc]
        if originColor == color:
            return image
        ROW = len(image)
        COL = len(image[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def traverse(r, c):
            if not(ROW>r>=0 and COL>c>=0 and image[r][c]==originColor):
                return
            image[r][c] = color
            for dr, dc in directions:
                traverse(r+dr, c+dc)
        traverse(sr, sc)
        return image

# using bfs and "deque" could make it faster
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if color == original_color:
            return image
        m = len(image)
        n = len(image[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        image[sr][sc] = color
        queue = deque([[sr, sc]])
        while queue:
            x, y = queue.popleft()
            for dir in directions:
                dx, dy = dir
                nxt_x = x+dx
                nxt_y = y+dy
                if m>nxt_x>=0 and n>nxt_y>=0 and image[nxt_x][nxt_y] == original_color:
                    image[nxt_x][nxt_y] = color
                    queue.append([nxt_x, nxt_y])
        return image

# bfs using tuple
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW = len(image)
        COL = len(image[0])
        originColor = image[sr][sc]
        if color == originColor:
            return image
        image[sr][sc] = color
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        qu = deque([(sr, sc)])
        
        while qu:
            r, c = qu.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if ROW>nr>=0 and COL>nc>=0 and image[nr][nc] == originColor:
                    image[nr][nc] = color
                    qu.append((nr, nc))
        return image

# bfs
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if color == image[sr][sc]:
#             return image
#         m = len(image)
#         n = len(image[0])
#         directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
#         original_color = image[sr][sc]
#         image[sr][sc] = color
#         curr = [[sr, sc]]
#         while curr:
#             nxt = []
#             for coord in curr:
#                 x, y = coord
#                 for dir in directions:
#                     dx, dy = dir
#                     nxt_x = x+dx
#                     nxt_y = y+dy
#                     if m>nxt_x>=0 and n>nxt_y>=0 and image[nxt_x][nxt_y] == original_color:
#                         image[nxt_x][nxt_y] = color
#                         nxt.append([nxt_x, nxt_y])
#                 curr = nxt
#         return image

if __name__ =='__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    sol = Solution()
    print(sol.floodFill(image, sr, sc, color))