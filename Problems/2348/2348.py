from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0 and l == -1:
                l = i
            elif num != 0 and l != -1:
                res += (1 + (i - l)) * (i - l) // 2
                l = -1
        if l != -1:
            res += (1 + (len(nums) - l)) * (len(nums) - l) // 2
        return res


nums = [1,3,0,0,2,0,0,4]
sol = Solution()
print(sol.zeroFilledSubarray(nums))
