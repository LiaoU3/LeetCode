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