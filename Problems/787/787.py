from typing import List
from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        adj = defaultdict(list)
        for start, end, cost in flights:
            adj[start].append((end, cost))

        costs = [float("Inf")] * n
        q = deque([(src, 0)])

        for _ in range(k + 1):
            q_len = len(q)
            for _ in range(q_len):
                city, cost = q.popleft()
                for nxt_city, nxt_cost in adj[city]:
                    if nxt_cost + cost < costs[nxt_city]:
                        q.append((nxt_city, nxt_cost + cost))
                        costs[nxt_city] = nxt_cost + cost

        return costs[dst] if costs[dst] != float("Inf") else -1

sol = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(sol.findCheapestPrice(n, flights, src, dst, k))