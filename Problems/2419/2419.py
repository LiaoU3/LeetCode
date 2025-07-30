class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        curr = res = 0
        for num in nums:
            if num == target:
                curr += 1
                res = max(res, curr)
            else:
                curr = 0
        return res
