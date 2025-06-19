class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        start = nums[0]
        for num in nums:
            if num > start + k:
                start = num
                res += 1
        return res

# TLE
# class Solution:
#     def partitionArray(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         dp = [float("Inf")] * len(nums)
#         dp[0] = 1
#         for i, num in enumerate(nums):
#             for j in range(i, -1, -1):
#                 dp[i] = min(dp[i], dp[j] + 1)
#                 if num - k > nums[j]:
#                     break
#             else:
#                 dp[i] = 1
#         return dp[-1]