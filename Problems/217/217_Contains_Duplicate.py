from typing import List


# Use set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash_table = {}
#         for num in nums:
#             if num in hash_table:
#                 return True
#             else:
#                 hash_table[num] = 1
#         return False
