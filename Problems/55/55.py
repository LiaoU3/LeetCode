from typing import List

# Instead of moving from the start, we move the goal back to the start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0

# Still not fast enough, but this is the improvement of the next solution
# O(n ^ 2)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}  # not in: not visted, False: Fail, True: Success
        def backtrack(i):
            if i in cache:
                return cache[i]
            if i >= len(nums) - 1:
                return True
            for j in range(i + nums[i], i, -1):
                if j in cache:
                    return cache[j]
                if backtrack(j):
                    cache[j] = True
                    return True
                else:
                    cache[j] = False
            return False
        return backtrack(0)


# Not Fast enough
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         visited = set()

#         def dfs(i):
#             if i >= len(nums) - 1:
#                 return True
#             if i in visited:
#                 return False
#             visited.add(i)
#             if i > 0 and nums[i] < nums[i - 1]:  # If the previsous one did not make it and current steps are smaller than the previous one, there is no way that current one could make it.
#                 return False 
#             for j in range(1, nums[i] + 1):
#                 if dfs(i + j):
#                     return True
#             return False
#         return dfs(0)

# TLE
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         visited = set()
        
#         def dfs(i):
#             if i >= len(nums) - 1:
#                 return True
#             if i in visited:
#                 return False
#             visited.add(i)
#             for j in range(1, nums[i] + 1):
#                 if dfs(i + j):
#                     return True
#             return False
#         return dfs(0)

# LTE
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         dp = [False] * len(nums)
#         dp[0] = True
#         for i in range(len(nums)):
#             if nums[i] == 0 or dp[i] == False:
#                 continue
#             for j in range(1, nums[i] + 1):
#                 if i + j >= len(nums):
#                     break
#                 dp[i + j] = True
#         return dp[-1]

sol = Solution()
nums = [2,3,1,1,4]
print(sol.canJump(nums))