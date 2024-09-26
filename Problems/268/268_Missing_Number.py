from typing import List

# bit manipulation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = 0
        for i, num in enumerate(nums):
            ret ^= i
            ret ^= num
        ret ^= i+1
        return ret

# using Arithmetic sequence formula
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         total = len(nums)*(len(nums)+1)//2
#         return total - sum(nums)

# It can be improved by Arithmetic sequence formula
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         total = 0
#         for i in range(len(nums) + 1):
#             total += i
#         for num in nums:
#             total -= num
#         return total