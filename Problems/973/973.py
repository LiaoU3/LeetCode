class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (distance, [x, y]))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
