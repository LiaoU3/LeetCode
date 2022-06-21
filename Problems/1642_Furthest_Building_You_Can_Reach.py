from typing import List
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        highers = [0]*ladders
        heapq.heapify(highers)
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff>0:
                if ladders and diff>highers[0]:
                    brick = heapq.heappushpop(highers, diff)
                    bricks -= brick
                else:
                    bricks -= diff
                if bricks<0:
                    return i-1
        return len(heights)-1

if __name__ =='__main__':
    heights = [4,2,7,6,9,14,12]
    bricks  = 5
    ladders = 1
    sol = Solution()
    print(sol.furthestBuilding(heights, bricks, ladders))