from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if num in table.keys():
                return [table[num], i]
            table[target-num] = i


# Time Complexity O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = number, value = index
        hash_table = {}
        for i in range(len(nums)):
            to_find_num = target - nums[i]
            if to_find_num in hash_table.keys():
                return[hash_table[to_find_num], i] 
            else:
                hash_table[nums[i]] = i

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             to_find_num = target - nums[i]
#             if to_find_num in nums[:i] or to_find_num in nums[i+1:]:
#                 ans.append(i)
#                 ans.append(nums.index(to_find_num, i+1))
#                 return ans
#                 break