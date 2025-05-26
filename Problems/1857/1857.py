class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adjs = defaultdict(list)
        for u, v in edges:
            adjs[u].append(v)

        counter = defaultdict(dict)
        visited = {}
        # Not in the set: not ever visited yet
        # True: visited and visiting
        # False: visisted but not visisting
        def dfs(node):
            if node in visited:
                if visited[node]:
                    return -1
                else:
                    return counter[node]
            visited[node] = True
            if colors[node] not in counter[node]:
                counter[node][colors[node]] = 0
            counter[node][colors[node]] += 1

            for nxt in adjs[node]:
                if dfs(nxt) == -1:
                    return -1
                for color, cnt in counter[nxt].items():
                    if color not in counter[node]:
                        counter[node][color] = 0
                    counter[node][color] = max(counter[node][color], cnt + (1 if color == colors[node] else 0))

            visited[node] = False
            return counter[node]

        res = 0
        for i in range(len(colors)):
            if dfs(i) == -1:
                return -1
            res = max(res, max(counter[i].values()))

        return res
