class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
            parent[p2] = p1
            rank[p1] += rank[p2]
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]