from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        hm = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                hm[stop].append(bus)

        if not hm[source] or not hm[target]:
            return -1
        # 0: unused, 1: used
        busStatus = [0] * len(routes)
        
        currStop = deque([source])
        cnt = 0
        while currStop:
            length = len(currStop)
            cnt += 1
            for _ in range(length):
                stop = currStop.popleft()
                for bus in hm[stop]:
                    if busStatus[bus]:
                        continue
                    busStatus[bus] = 1
                    for otherStop in routes[bus]:
                        if otherStop == target:
                            return cnt
                        currStop.append(otherStop)
        return -1

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # every busStop that busNum will stop
        busStop = defaultdict(set)
        for busNum, route in enumerate(routes):
            for stop in route:
                busStop[stop].add(busNum)
        
        qu = deque([source])
        # set usedBus is for if the bus is used than we don't have to use it anymore
        usedBus = set()
        cnt = 0
        while qu:
            cnt += 1
            length = len(qu)
            for _ in range(length):
                curr = qu.popleft()
                for busNum in busStop[curr]:
                    if busNum in usedBus:
                        continue
                    usedBus.add(busNum)
                    for stop in routes[busNum]:
                        if stop == target:
                            return cnt
                        qu.append(stop)
        return -1

# TLE
# class Solution:
#     def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
#         if source == target:
#             return 0

#         # every busStop that busNum will stop
#         busStop = defaultdict(set)
#         for busNum, route in enumerate(routes):
#             for stop in route:
#                 busStop[stop].add(busNum)
        
#         qu = deque([source])
#         visited = {source}
#         cnt = 0
#         while qu:
#             cnt += 1
#             length = len(qu)
#             for _ in range(length):
#                 curr = qu.popleft()
#                 for busNum in busStop[curr]:
#                     for stop in routes[busNum]:
#                         if stop == target:
#                             return cnt
#                         if stop not in visited:
#                             qu.append(stop)
#                             visited.add(stop)
#         return -1


if __name__ == '__main__':
    sol = Solution()
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    print(sol.numBusesToDestination(routes, source, target))