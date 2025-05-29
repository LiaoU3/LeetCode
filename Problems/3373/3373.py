class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adjs1 = defaultdict(list)
        for u, v in edges1:
            adjs1[u].append(v)
            adjs1[v].append(u)
    
        adjs2 = defaultdict(list)
        for u, v in edges2:
            adjs2[u].append(v)
            adjs2[v].append(u)

        evens = set()
        def dfs(adjs, prev, curr, depth):
            total = 0
            if depth % 2 == 0:
                total += 1
                evens.add(curr)
            for nxt in adjs[curr]:
                if nxt != prev:
                    total += dfs(adjs, curr, nxt, depth + 1)
            return total 

        targeted = dfs(adjs2, -1, 0, 1)
        max2 = max(targeted, len(edges2) + 1 - targeted)

        res = [0] * (len(edges1) + 1)
        evens = set()
        targeted = dfs(adjs1, -1, 0, 0)
        if 0 in evens:
            for i in range(len(edges1) + 1):
                if i in evens:
                    res[i] = targeted + max2
                else:
                    res[i] = len(edges1) + 1 - targeted + max2
        else:
            for i in range(len(edges1) + 1):
                if i not in evens:
                    res[i] = targeted + max2
                else:
                    res[i] = len(edges1) + 1 - targeted + max2

        return res


# TLE
# class Solution:
#     def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
#         adjs1 = defaultdict(list)
#         for u, v in edges1:
#             adjs1[u].append(v)
#             adjs1[v].append(u)

#         adjs2 = defaultdict(list)
#         for u, v in edges2:
#             adjs2[u].append(v)
#             adjs2[v].append(u)

#         def dfs(adjs, prev, curr, depth):
#             total = 0
#             if depth % 2 == 0:
#                 total += 1
#             for nxt in adjs[curr]:
#                 if nxt != prev:
#                     total += dfs(adjs, curr, nxt, depth + 1)
#             return total 

#         max2 = 0
#         for i in range(len(edges2) + 1):
#             max2 = max(max2, dfs(adjs2, -1, i, 1))

#         res = []
#         for i in range(len(edges1) + 1):
#             res.append(dfs(adjs1, -1, i, 0) + max2)

#         return res
