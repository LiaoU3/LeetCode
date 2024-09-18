class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            h_l = height[l]
            h_r = height[r]
            res = max(res, min(h_l, h_r) * (r - l))
            if h_l < h_r:
                l += 1
            else:
                r -= 1
        return res

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l = 0
#         r = len(height) - 1
#         volume_max = 0
#         while(l<r):
#             volume_max = max((r-l)*min(height[l], height[r]), volume_max)
#             if height[l] > height[r]:
#                 r -= 1
#             else:
#                 l += 1
#         return volume_max