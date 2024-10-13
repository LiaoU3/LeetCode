from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        seen = set()
        cnt = 0
        def dfs(num):
            if num in seen:
                return
            seen.add(num)
            for next_num in graph[num]:
                dfs(next_num)

        for i in range(n):
            if i in seen:
                continue
            cnt += 1
            dfs(i)
        return cnt