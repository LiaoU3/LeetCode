from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
            if course == pre:  # Return earilier when there is an obvious loop
                return False

        seen = set()
        def dfs(course):
            if not graph[course]:
                return True
            if course in seen:
                return False
            seen.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            graph[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# Slow
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set([i for i in range(numCourses)])
        course = defaultdict(list)  # key: course, val: [prerequisite1, prerequisite2, ...]
        for c, p in prerequisites:
            course[c].append(p)
            if c in taken:
                taken.remove(c)

        seen = set()
        def dfs(c):
            if c in taken:
                return True
            if c in seen:
                return False
            seen.add(c)
            for p in course[c]:
                if not dfs(p):
                    return False
            taken.add(c)
            return True

        for i in range(numCourses):
            seen = set()
            dfs(i)
        return len(taken) == numCourses


s = Solution()
numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
print(s.canFinish(numCourses, prerequisites))
