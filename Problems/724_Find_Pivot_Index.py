class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        leftSum = 0
        rightSum = sum(nums[1:])
        if leftSum == rightSum:
            return pivot
        while pivot<len(nums)-1:
            leftSum += nums[pivot]
            rightSum-= nums[pivot+1]
            pivot += 1
            if leftSum == rightSum:
                return pivot
        return -1