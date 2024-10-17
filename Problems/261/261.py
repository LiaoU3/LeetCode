class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        seen = set()
        def dfs(node, pre):
            if node in seen:
                return False
            seen.add(node)
            for n2 in graph[node]:
                if n2 == pre:
                    continue
                if not dfs(n2, node):
                    return False
            return True
        
        if dfs(0, -1) and len(seen) == n:
            return True
        else:
            return False