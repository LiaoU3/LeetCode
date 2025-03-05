from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  # (height, index) strict incresing stack

        for i in range(len(heights)):
            j = i
            while stack and stack[-1][0] > heights[i]:
                h, j = stack.pop()
                res = max(res, ((i - j) * h))
            stack.append((heights[i], j))
        
        while stack:
            h, i = stack.pop()
            res = max(res, (len(heights) - i) * h)

        return res


sol = Solution()
heights = [1,2,2]
print(sol.largestRectangleArea(heights))
