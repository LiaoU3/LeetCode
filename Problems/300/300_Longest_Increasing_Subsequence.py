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

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        def binary_search(l, r, target):
            if l > r:
                return l
            m = (l + r) // 2
            if dp[m] == target:
                return m
            elif dp[m] > target:
                return binary_search(l, m - 1, target)
            else:
                return binary_search(m + 1, r, target)
        
        for num in nums:
            l = 0
            r = len(dp) - 1
            i = binary_search(l, r, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)


# Time Complexity : O(N**2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


# TLE O(N**2)
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


# TLE O(N**2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def backtrack(i, num):
            if i == len(nums):
                return 0
            # without nums[i + 1]
            res = backtrack(i + 1, num)
            # with nums[i + 1]
            if nums[i] > num:
                res = max(res, backtrack(i + 1, nums[i]) + 1)
            return res
        return backtrack(0, -float("Inf"))


def main():
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))

if __name__ == '__main__':
    main()