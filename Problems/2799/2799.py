class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        remain = len(set(nums))


        curr = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            curr[nums[r]] += 1
            if curr[nums[r]] == 1:
                remain -= 1
            while remain == 0:
                res += len(nums) - r
                curr[nums[l]] -= 1
                if curr[nums[l]] == 0:
                    remain += 1
                l += 1

        return res

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))

        res = 0
        for i in range(len(nums)):
            remain = target
            curr = defaultdict(int)
            for j in range(i, len(nums)):
                num = nums[j]
                curr[num] += 1
                if curr[num] == 1:
                    remain -= 1
                if remain == 0:
                    res += 1

        return res
