class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adjs1 = defaultdict(list)
        for u, v in edges1:
            adjs1[u].append(v)
            adjs1[v].append(u)

        adjs2 = defaultdict(list)
        for u, v in edges2:
            adjs2[u].append(v)
            adjs2[v].append(u)

        def dfs(adjs, prev, curr, depth):
            if depth < 0:
                return 0
            total = 1
            for nxt in adjs[curr]:
                if nxt != prev:
                    total += dfs(adjs, curr, nxt, depth - 1)
            return total

        max2 = 0
        for i in range(len(edges2) + 1):
            max2 = max(max2, dfs(adjs2, -1, i, k - 1))

        res = []
        for i in range(len(edges1) + 1):
            res.append(dfs(adjs1, -1, i, k) + max2)

        return res


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adjs1 = defaultdict(set)
        for u, v in edges1:
            adjs1[u].add(v)
            adjs1[v].add(u)

        adjs2 = defaultdict(set)
        for u, v in edges2:
            adjs2[u].add(v)
            adjs2[v].add(u)

        seen = set()
        def dfs(adjs, node, depth):
            if node in seen:
                return 0
            seen.add(node)
            if depth < 0:
                return 0
            total = 1
            for nxt in adjs[node]:
                total += dfs(adjs, nxt, depth - 1)
            return total

        max2 = 0
        for i in range(len(edges2) + 1):
            seen = set()
            max2 = max(max2, dfs(adjs2, i, k - 1))

        res = []
        for i in range(len(edges1) + 1):
            seen = set()
            res.append(dfs(adjs1, i, k) + max2)

        return res
