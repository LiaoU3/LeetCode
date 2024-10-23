class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)  # Max height on the left side
        right = [0] * len(height)  # Max height on the right side
        curr_max = 0
        for i in range(len(height)):
            h = height[i]
            left[i] = curr_max
            curr_max = max(curr_max, h)
        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            right[i] = curr_max
            curr_max = max(curr_max, height[i])
        total = 0
        for i in range(len(height)):
            water = min(left[i], right[i]) - height[i]
            if water > 0:
                total += water
        return total