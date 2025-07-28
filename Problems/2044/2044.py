class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for num in nums:
            target |= num

        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            if curr > target:
                return 0
            if curr == target:
                return 1 << (len(nums) - i)
            take = dfs(i + 1, curr | nums[i])
            no_take = dfs(i + 1, curr)

            return take + no_take

        return dfs(0, 0)
