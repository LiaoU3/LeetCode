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
#         self.res = 0
#         def find(i, total):
#             if i == len(nums):
#                 if total == target:
#                     self.res += 1
#                 return
#             find(i + 1, total + nums[i])
#             find(i + 1, total - nums[i])
#         find(0, 0)
#         return self.res