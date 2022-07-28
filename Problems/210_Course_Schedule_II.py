from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        # 0 : unsearch, 1 : searching, 2 : searched
        state = [0]*numCourses
        
        courseOrder = []
        self.isPossible = True
        def dfs(course):
            if not self.isPossible:
                return
            state[course] = 1
            for c in graph[course]:
                if state[c] == 0:
                    dfs(c)
                elif state[c]== 1:
                    self.isPossible = False
            courseOrder.append(course)
            state[course] = 2
        
        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)
        
        return courseOrder if self.isPossible else []