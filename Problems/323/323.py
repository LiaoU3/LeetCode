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


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            """Return the parent of the node and update the parent list"""
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]        

        def union(node1, node2):
            """Union 2 nodes together"""
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return True
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            parent[p2] = p1
            rank[p1] += rank[p2]
            return False

        res = n
        for node1, node2 in edges:
            if not union(node1, node2):
                res -= 1

        return res
