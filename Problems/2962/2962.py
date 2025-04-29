class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value = max(nums)
        cnt = 0
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == max_value:
                cnt += 1
            while cnt >= k:
                if nums[l] == max_value:
                    cnt -= 1
                l += 1
            res += l
        return res
