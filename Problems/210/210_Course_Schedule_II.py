from collections import defaultdict
from typing import List

# Cleanest solution
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        seen = {}  # key: course, val: True -> currently visited, False -> Visited in another round.
        res = []
        def dfs(course):
            if course in seen:
                return seen[course]
            seen[course] = True
            for nxt in adj[course]:
                if dfs(nxt):
                    return True
            seen[course] = False
            res.append(course)
            return False

        for i in range(numCourses):
            if dfs(i):
                return []
        return res

# Cleaner solution
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        res = []
        state = [0] * numCourses  # 0: not visited, 1: visting, 2: visited
        def dfs(i):
            if state[i] == 1:
                return False
            if state[i] == 2:
                return True
            state[i] = 1
            for pre in graph[i]:
                if not dfs(pre):
                    return False
            state[i] = 2
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)
#         for c1, c2 in prerequisites:
#             graph[c1].append(c2)

#         # 0 : unsearch, 1 : searching, 2 : searched
#         state = [0]*numCourses
        
#         courseOrder = []
#         self.isPossible = True
#         def dfs(course):
#             if not self.isPossible:
#                 return
#             state[course] = 1
#             for c in graph[course]:
#                 if state[c] == 0:
#                     dfs(c)
#                 elif state[c]== 1:
#                     self.isPossible = False
#             courseOrder.append(course)
#             state[course] = 2
        
#         for i in range(numCourses):
#             if state[i] == 0:
#                 dfs(i)
        
#         return courseOrder if self.isPossible else []

numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
sol = Solution()
print(sol.findOrder(numCourses, prerequisites))