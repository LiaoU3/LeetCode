from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum

# Memory Limit Exceeded
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
#         max_sum = nums[0]
#         for i in range(len(nums)):
#             dp[i][i] = nums[i]
#             max_sum = max(max_sum, nums[i])
#             for j in range(i+1, len(nums)):
#                 dp[i][j] = dp[i][j-1] + nums[j]
#                 max_sum = max(max_sum, dp[i][j])
#         return max_sum

if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))