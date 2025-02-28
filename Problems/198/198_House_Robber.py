class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0, 0, 0] + nums

        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])
        
        return max(nums[-2:])

class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, m):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]