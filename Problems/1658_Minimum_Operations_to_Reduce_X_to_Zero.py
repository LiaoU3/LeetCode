from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        max_count = -1
        left, right, total = 0, 0, 0

        while right < len(nums):
            total += nums[right]
            while total >= target:
                if total == target:
                    max_count = max(max_count, right-left+1)
                total -= nums[left]
                left += 1
            right += 1

        if max_count == -1:
            return -1
        else:
            return len(nums) - max_count


# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         target = sum(nums) - x
#         if nums[0]>x and nums[-1]>x:
#             return -1
#         if target == 0:
#             return len(nums)
#         max_count = -1

#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 total += nums[j]
#                 if total == target:
#                     max_count = max(max_count, j-i+1)
#                 elif total > target:
#                     break
#         if max_count == float('-Inf'):
#             return -1
#         else:
#             return len(nums) - max_count

if __name__ == '__main__':
    sol = Solution()
    nums = [5,2,3,1,1]
    x = 5
    print(sol.minOperations(nums, x))