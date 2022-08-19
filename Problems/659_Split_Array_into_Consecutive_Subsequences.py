from typing import List
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in sorted(c.keys()):
            while c[i] > 0:
                j = i
                length = 0
                currCnt = 0
                while c[j] >= currCnt:
                    currCnt = c[j]
                    c[j] -= 1
                    length += 1
                    j += 1
                if length < 3:
                    return False
        return True


# TLE
# class Solution:
#     def isPossible(self, nums: List[int]) -> bool:
#         m = len(nums)
#         if m < 3:
#             return False
#         LastCount = [[0, 0] for _ in range(m//3)]
#         length = 0
#         for num in nums:
#             for i in range(length-1, -1, -1):
#                 if LastCount[i][0] + 1 == num:
#                     LastCount[i][0] = num
#                     LastCount[i][1] += 1
#                     break
#             else:
#                 if length == m//3:
#                     return False
#                 LastCount[length][0] = num
#                 LastCount[length][1] += 1
#                 length += 1
#         for i in range(length):
#             if LastCount[i][1] < 3:
#                 return False
#         return True

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,3,4,5]
    print(sol.isPossible(nums))