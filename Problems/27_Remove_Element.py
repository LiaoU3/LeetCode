class Solution:
    def removeElement(self, nums, val):
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end = end - 1
            else:
                start +=1
        return start

# solution = Solution()
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(solution.removeElement(nums, val))