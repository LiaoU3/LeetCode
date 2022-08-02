from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        
        def traverse(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    traverse(j)

        cnt = 0
        for i in range(n):
            if not visited[i]:
                cnt += 1
                traverse(i)
        return cnt

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         # -1 : unvisited, 0 : first province, 1 : second province etc.
#         cities = [-1]*n
        
#         def traverse(i, maxGroup):
#             cities[i] = maxGroup
#             for j in range(n):
#                 if isConnected[i][j] == 1 and cities[j] == -1:
#                     traverse(j, maxGroup)

#         maxGroup = -1
#         for i in range(n):
#             if cities[i] != -1:
#                 continue
#             maxGroup += 1
#             traverse(i, maxGroup)
#         return maxGroup+1

if __name__ == '__main__':
    sol = Solution()
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.findCircleNum(isConnected))