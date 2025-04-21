from typing import List


# Prefix & Suffix Arrays
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        
        seen_max = -float("Inf")
        for i in range(len(height)):
            seen_max = max(seen_max, height[i])
            left[i] = seen_max

        seen_max = -float("Inf")
        for i in range(len(height) - 1, -1, -1):
            seen_max = max(seen_max, height[i])
            right[i] = seen_max

        res = 0
        for i, h in enumerate(height):
            res += min(left[i], right[i]) - h

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
