from typing import List


# Prefix & Suffix Arrays
class Solution:
    def trap(self, height: List[int]) -> int:

        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])

        right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        res = 0
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]

        return res


# Strictly decreasin
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  #  (h, i) strictly decreasing stack

        res = 0
        for i, h in enumerate(height):
            floor = 0
            while stack and stack[-1][0] <= h:
                left_h, left_i = stack.pop()
                res += (left_h - floor) * (i - left_i - 1)
                floor = left_h
            if stack:
                res += (h - floor) * (i - stack[-1][1] - 1)
            stack.append((h, i))
        return res


height = [4, 2, 0, 3, 2, 5]
s = Solution()
print(s.trap(height))
