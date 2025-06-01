import math

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(a, b):
            if a < 0 or b < 0 or a < b:
                return 0
            return math.comb(a, b)

        total = comb(n + 2, 2)

        over1 = comb(n - (limit + 1) + 2, 2)
        over2 = comb(n - 2 * (limit + 1) + 2, 2)
        over3 = comb(n - 3 * (limit + 1) + 2, 2)

        return total - 3 * over1 + 3 * over2 - over3



# TLE
# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         def backtrack(child, left):
#             if child == 2:
#                 return 1 if left <= limit else 0
#             res = 0
#             for i in range(min(left, limit) + 1):
#                 res += backtrack(child + 1, left - i)
#             return res
#         return backtrack(0, n)

sol = Solution()
n = 5
limit = 2
print(sol.distributeCandies(n, limit))
