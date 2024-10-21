from typing import List
from heapq import heappop, heappush
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        klargest = [float('-Inf')]*k
        heapq.heapify(klargest)
        for num in nums:
            heapq.heappushpop(klargest, num)
        return klargest[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heappush(h, num)
            if len(h) > k:
                heappop(h)
        return heappop(h)

sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(sol.findKthLargest(nums, k))