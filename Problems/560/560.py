class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        res = 0
        total = 0
        for num in nums:
            res += prefix_sum[k - num]
            total += num
            prefix_sum[total] += 1
        return res

# Sliding windows does not work here
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res = 0
#         l = 0
#         total = 0
#         for r in range(len(nums)):
#             total += nums[r]
#             while l < r and total > k:
#                 total -= nums[l]
#                 l += 1
#             if total == k:
#                 res += 1
#         return res