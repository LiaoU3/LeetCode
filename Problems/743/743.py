class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = collections.defaultdict(list)
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
            total_time = max(total_time, time)
            for target, target_time in network[source]:
                if target in seen:
                    continue
                heapq.heappush(min_heap, (time + target_time, target))
        return total_time if len(seen) == n else -1
