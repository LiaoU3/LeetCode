from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]
            add = backtrack(i + 1, total + nums[i])
            subtract = backtrack(i + 1, total - nums[i])
            cache[(i, total)] = add + subtract
            return cache[(i, total)]
        return backtrack(0, 0)


# TLE
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
#         def backtrack(i, total):
#             if i == len(nums):
#                 if total == target:
#                     return 1
#                 else:
#                     return 0
#             return backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
        
#         return backtrack(0, 0)

nums = [1,1,1,1,1]
target = 3
sol = Solution()
print(sol.findTargetSumWays(nums, target))