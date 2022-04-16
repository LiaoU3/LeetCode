class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums

    def quicksort(self, nums,left,right):
        if left < right:
            l = left
            # r = right

            # I know it's not necessary, but you will get TLE in test 11/13, if you don't do this below
            pivot = (left + right) // 2

            nums[pivot], nums[right] = nums[right], nums[pivot]

            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            nums[l], nums[right] = nums[right], nums[l]

            self.quicksort(nums, left, l-1)
            self.quicksort(nums, l+1,  right)