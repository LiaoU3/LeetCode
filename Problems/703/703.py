class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.large = []
        for i, num in enumerate(nums):
            if i == k:
                return
            heapq.heappush(self.large, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.large, val)
        if len(self.large) > self.k:
            heapq.heappop(self.large)
        return self.large[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)