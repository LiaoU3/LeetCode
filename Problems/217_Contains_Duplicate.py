from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums:
            if num in hash_table:
                return True
            else:
                hash_table[num] = 1
        return False