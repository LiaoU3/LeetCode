from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)
        for source, target, time in times:
            network[source].append((target, time))
        total_time = 0
        seen = set()
        min_heap = [(0, k)]
        while min_heap:
            time, source = heapq.heappop(min_heap)
            if source in seen:
                continue
            seen.add(source)
            total_time = time
            for target, target_time in network[source]:
                if target in seen:
                    continue
                heapq.heappush(min_heap, (time + target_time, target))
        return total_time if len(seen) == n else -1


# Wrong
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        networks = defaultdict(list)  # key: start, val: [[end1, time1], [end2, time2] ... ]
        nodes = set()
        for start, end, time in times:
            networks[start].append([end, time])
            nodes.add(start)
            nodes.add(end)
        seen = set()
        seen.add(k)
        curr = deque()
        curr.extend(networks[k])
        res = 0
        while curr:
            res += 1
            length = len(curr)
            for _ in range(length):
                end, time = curr.popleft()
                if end in seen:
                    continue
                if time - 1 == 0:
                    seen.add(end)
                    curr.extend(networks[end])
                else:
                    curr.append([end, time - 1])
        if len(seen) == len(nodes):
            return res
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    times = [[1,2,1],[2,1,3]]
    n = 2
    k = 2
    print(s.networkDelayTime(times, n, k))
