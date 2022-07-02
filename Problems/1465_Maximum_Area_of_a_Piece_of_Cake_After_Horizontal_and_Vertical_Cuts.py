class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHorizontal = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            maxHorizontal = max(maxHorizontal, horizontalCuts[i]-horizontalCuts[i-1])
        maxHorizontal = max(maxHorizontal, h-horizontalCuts[-1])

        maxVertical = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            maxVertical = max(maxVertical, verticalCuts[i]-verticalCuts[i-1])
        maxVertical = max(maxVertical, w-verticalCuts[-1])
        # print(maxHorizontal, maxVertical)
        return maxHorizontal*maxVertical %(10**9+7)