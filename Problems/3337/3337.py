from typing import List


# TLE
# class Solution:
#     def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
#         MOD = 10 ** 9 + 7
#         counter = [0] * 26
#         for c in s:
#             counter[ord(c) - ord("a")] += 1

#         for _ in range(t):
#             new_counter = [0] * 26
#             for i, cnt in enumerate(counter):
#                 if cnt:
#                     if i + nums[i] < 26:
#                         for j in range(i + 1, i + nums[i] + 1):
#                             new_counter[j] += cnt
#                     else:
#                         for j in range(i + 1, 26):
#                             new_counter[j] += cnt
#                         over_flow = i + nums[i] - 25
#                         for j in range(over_flow):
#                             new_counter[j] += cnt
#             for i in range(len(new_counter)):
#                 new_counter[i] %= MOD
#             counter = new_counter
#             print(counter)
#         return sum(counter) % MOD

s = "u"
t = 5
nums = [1,1,2,2,3,1,2,2,1,2,3,1,2,2,2,2,3,3,3,2,3,2,3,2,2,3]
sol = Solution()
print(sol.lengthAfterTransformations(s, t, nums))
