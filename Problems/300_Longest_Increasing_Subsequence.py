from typing import List

# Time Complexity : O(N*Log(N))
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def binary_search_insert_index(d, n):
            left = 0
            right = len(d) - 1
            while left <= right:
                middle = (left+right)//2
                if n > d[middle]:
                    left = middle + 1
                elif n < d[middle]:
                    right = middle - 1
                else:
                    return middle
            return left
        
        dp = []
        for num in nums:
            i = binary_search_insert_index(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)


# Time Complexity : O(N*Log(N))
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLen = 0
        n = len(nums)
        dp = [0] * n

        def binarySearch(left, right, target):
            if left > right:
                return left
            middle = (left + right) // 2
            if dp[middle] == target:
                return middle
            elif dp[middle] > target:
                return binarySearch(left, middle-1, target)
            else:
                return binarySearch(middle+1, right, target)

        for i in range(n):
            index = binarySearch(0, maxLen-1, nums[i])
            if index == maxLen:
                dp[maxLen] = nums[i]
                maxLen += 1
            else:
                dp[index] = nums[i]
        return maxLen


# Time Complexity : O(N**2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLen = 0
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            for j in range(maxLen):
                if nums[i] <= dp[j]:
                    dp[j] = nums[i]
                    break
            else:
                dp[maxLen] = nums[i]
                maxLen += 1
        print(dp)
        return maxLen

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         maxLen = 1
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]
        
#         for i in range(1, n):
#             for j in range(maxLen):
#                 if nums[i] <= dp[j]:
#                     dp[j] = nums[i]
#                     break
#             else:
#                 dp[maxLen] = nums[i]
#                 maxLen += 1
#         print(dp)
#         return maxLen

# Time Complexity : O(N**2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

def main():
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))

if __name__ == '__main__':
    main()