from os import remove
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        curr_sum, max_sum = 0, 0
        left = 0
        for num in nums:
            while num in seen:
                seen.remove(num[left])
                curr_sum -= num
                left += 1
            curr_sum += num
            seen.add(num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

# class Solution:
#     def maximumUniqueSubarray(self, nums: List[int]) -> int:
#         left = 0
#         right = 0
#         max_sub = 0
#         total = 0
#         while right < len(nums):
#             if nums[right] not in nums[left:right]:
#                 total += nums[right]
#                 max_sub = max(max_sub, total)
#             else:
#                 while nums[right] in nums[left:right]:
#                     total -= nums[left]
#                     left += 1
#                 total += nums[right]
#             right += 1
#         return max_sub

if __name__ == '__main__':
    sol = Solution()
    nums = [4,2,4,5,6]
    print(sol.maximumUniqueSubarray(nums))