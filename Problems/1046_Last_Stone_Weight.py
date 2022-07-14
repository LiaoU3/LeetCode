# it can be simnplified because on top of the heap will always be the biggest number
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            heaviest = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if heaviest!=second:
                heapq.heappush(stones, heaviest-second)
        return -stones[0] if len(stones) else 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1<stone2:
                heapq.heappush(stones, stone1-stone2)
            elif stone2<stone1:
                heapq.heappush(stones, stone2-stone1)
        return -stones[0] if len(stones) else 0