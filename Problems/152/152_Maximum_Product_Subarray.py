class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i - 1][1] * nums[i], dp[i - 1][0] * nums[i])
            res = max(res, dp[i][0])
        return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = localMin = maxProduct = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                localMax, localMin = localMin, localMax
            localMax = max(localMax*nums[i], nums[i])
            localMin = min(localMin*nums[i], nums[i])
            maxProduct = max(maxProduct, localMax)
        return maxProduct

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = nums[0]
        localMin = nums[0]
        globalMax = nums[0]
        print(localMin, localMax, globalMax)
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                localMax, localMin = max(num, localMin * num), min(num, localMax * num)
            else:
                localMax, localMin = max(num, localMax * num), min(num, localMin * num)
            globalMax = max(globalMax, localMax)
            print(localMin, localMax, globalMax)
        return globalMax

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[-float("Inf"), float("Inf")] for _ in range(len(nums))]  # [Largest, Smallest]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        res = dp[0][0]
        for i in range(1, len(nums)):
            num = nums[i]
            dp[i][0] = max(num, num * dp[i - 1][0], num * dp[i - 1][1])
            dp[i][1] = min(num, num * dp[i - 1][0], num * dp[i - 1][1])
            res = max(res, dp[i][0])
        return res