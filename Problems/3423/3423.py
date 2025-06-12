class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = max(res, abs(nums[i] - nums[i - 1]))
        return res
