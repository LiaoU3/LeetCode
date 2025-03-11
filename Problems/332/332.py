class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, t in tickets:
            heappush(adj[s], t)

        res = []
        def dfs(curr):
            while adj[curr]:
                nxt = heappop(adj[curr])
                dfs(nxt)
            res.append(curr)

        dfs("JFK")
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:        
        directions = defaultdict(list)
        tickets.sort(reverse=True)
        for start, end in tickets:
            directions[start].append(end)
        res = []
        def dfs(curr):
            while directions[curr]:
                next_dest = directions[curr].pop()
                dfs(next_dest)
            res.append(curr)
        dfs("JFK")
        return res[::-1]

# TLE Solution
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         directions = collections.defaultdict(list)
#         tickets.sort()
#         for start, end in tickets:
#             directions[start].append(end)
#         res = ["JFK"]
#         def dfs(curr):
#             if len(res) == len(tickets) + 1:
#                 return True
#             if not directions[curr]:
#                 return False
#             for i, end in enumerate(directions[curr]):
#                 res.append(end)
#                 directions[curr].pop(i)
#                 if dfs(end):
#                     return True
#                 res.pop()
#                 directions[curr].insert(i, end)
#             return False
#         dfs("JFK")
#         return res
