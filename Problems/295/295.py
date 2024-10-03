class MedianFinder:

    def __init__(self):
        self.small_heap = []  # Max heap
        self.large_heap = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)
        
        if self.large_heap and (-self.small_heap[0] > self.large_heap[0]):
            max_from_small_heap = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, max_from_small_heap)
        
        if len(self.small_heap) > len(self.large_heap) + 1:
            max_from_small_heap = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, max_from_small_heap)
        elif len(self.large_heap) > len(self.small_heap):
            min_from_large_heap = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -min_from_large_heap)
   
    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        else:
            return -self.small_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()