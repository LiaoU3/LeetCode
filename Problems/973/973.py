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

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(i):
            return points[i][0] ** 2 + points[i][1] ** 2

        def partition(l, r):
            pivot_index = r
            pivot_distance = distance(pivot_index)
            i = l
            for j in range(l, r):
                if distance(j) < pivot_distance:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[pivot_index] = points[pivot_index], points[i]
            return i

        pivot_index = len(points)
        l = 0
        r = len(points) - 1
        while pivot_index != k:
            pivot_index = partition(l, r)
            if pivot_index > k:
                r = pivot_index - 1
            else:
                l = pivot_index + 1
        return points[:k]