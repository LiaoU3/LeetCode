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
        # Strictly decreasing
        stack = []  # (height, index)
        res = 0
        for i, h in enumerate(height):
            while stack and stack[-1][0] <= h:
                left_h, left_i = stack.pop()
                res += (i - left_i - 1) * (left_h - base)
                base = left_h
            else:
                if stack:
                    res += (i - stack[-1][1] - 1) * (h - base)
                    base = h
            stack.append((h, i))
            base = h
        return res


height = [4, 2, 0, 3, 2, 5]
s = Solution()
print(s.trap(height))
