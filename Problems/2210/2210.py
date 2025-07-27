from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_nums = []
        new_nums.append(nums[0])
        for num in nums[1:]:
            if num != new_nums[-1]:
                new_nums.append(num)
        res = 0
        for i in range(1, len(new_nums) - 1):
            if new_nums[i] > new_nums[i - 1] and new_nums[i] > new_nums[i + 1]:
                res += 1
            elif new_nums[i] < new_nums[i - 1] and new_nums[i] < new_nums[i + 1]:
                res += 1
        return res


sol = Solution()
nums = [2,4,1,1,6,5]
print(sol.countHillValley(nums))
