class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt += 1
            while cnt > 1:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            curr = r - l + 1 - cnt
            res = max(res, curr)
        return res if cnt != 0 else res - 1
