from operator import le
from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target)==1:
            return target[0]==1
        target = [-x for x in target]
        heapq.heapify(target)
        total = -sum(target)
        while True: 
            largest = -heapq.heappop(target)
            total -= largest
            if largest == 1:
                return True
            after = (largest-1) % total + 1
            heapq.heappush(target, -after)
            total += after
            if after < 1 or largest==after:
                return False

if __name__ =='__main__':
    sol = Solution()
    targets = [1,49,11,1,25,1,7]
    print(sol.isPossible(targets))