class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                    res = max(res, i - stack.pop())
        return res

# TLE
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i, num in enumerate(nums[1:]):
            if num < nums[stack[-1]]:
                i += 1
                stack.append(i)
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in stack:
                if nums[j] <= nums[i]:
                    res = max(res, i - j)
                    break
        return res

# Failed
# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         l = 0
#         r = len(nums) - 1
#         res = 0
#         while l < r:
#             if nums[l] > nums[r]:
#                 l += 1
#             else:
#                 res =  max(res, r - l)
#                 r -= 1
#         return res