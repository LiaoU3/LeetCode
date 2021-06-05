class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1

# solution = Solution()
# nums = [1, 1, 2]
# print(solution.removeDuplicates(nums))
# print(nums)