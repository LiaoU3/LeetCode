from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        point = 0
        for num in nums:
            if num != 0:
                nums[point] = num
                point += 1
        for i in range(point, len(nums)):
            nums[i] = 0
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         point_zero = len(nums) - 1
#         for i in range(len(nums)-1, -1, -1):
#             if nums[i] == 0:
#                 nums[i:point_zero] = nums[i+1:point_zero+1]
#                 nums[point_zero] = 0
#                 point_zero -= 1

if __name__ =='__main__':
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)