class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10 ** 9 + 7
        n = len(nums)
        
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        l, r = 0, n - 1
        res = 0

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow2[r - l]
                res %= MOD
                l += 1
        return res


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10 ** 9 + 7
        l = 0
        r = len(nums) - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 2 ** (r - l)
                res %= MOD
                l += 1
        return res