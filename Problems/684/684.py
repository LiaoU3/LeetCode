class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [ 1 for _ in range(len(edges) + 1)]
        
        # Find the parent and update it
        def find(node):
            if node != parents[node]:
                node = find(parents[node])
            return node
        # def find(node):
        #     p = parents[node]
        #     children = []
        #     while node != parents[node]:
        #         node = parents[node]
        #         children.append(node)
        #     for child in children:
        #         parents[child] = node
        #     return node

        # Union 2 graphs together
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p2] = p1
                ranks[p2] += ranks[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]