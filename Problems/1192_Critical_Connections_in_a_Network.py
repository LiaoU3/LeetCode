from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def dfs(curr: int, parent: int, curr_step: int, min_step_list: List[int], res: List[List[int]], graph: defaultdict) -> int:

            min_step_list[curr] = curr_step+1

            for child in graph[curr]:
                # prevent from traverse to parent
                if child == parent:
                    continue

                # haven't been traversed
                if min_step_list[child] == -1:
                    min_step_list[curr] = min(min_step_list[curr], dfs(child, curr, curr_step+1, min_step_list, res,  graph))
                
                # have been traveresed
                else:
                    min_step_list[curr] = min(min_step_list[curr], min_step_list[child])
            
            if min_step_list[curr] == curr_step+1 and curr != 0:
                res.append([curr, parent])
            
            return min_step_list[curr]
        
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        min_step_list = [-1]*n
        res = []

        dfs(0, -1, 0, min_step_list, res, graph)
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    print(sol.criticalConnections(n, connections))