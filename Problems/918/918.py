from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min = global_min = float("Inf")
        curr_max = global_max = -float("Inf")
        for num in nums:
            curr_min = min(curr_min + num, num)
            global_min = min(global_min, curr_min)
            curr_max = max(curr_max + num, num)
            global_max = max(global_max, curr_max)

        return max(global_max, sum(nums) - global_min) if global_max > 0 else global_max


nums = [5, -3, 5]
sol = Solution()
print(sol.maxSubarraySumCircular(nums))
