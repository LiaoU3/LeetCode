class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        volume_max = 0
        while(l<r):
            volume_max = max((r-l)*min(height[l], height[r]), volume_max)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return volume_max