# O(N ^ 3)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def backtrack(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            max_coin = 0
            for i in range(l, r + 1):
                l_balloon = nums[l - 1]
                r_balloon = nums[r + 1]
                coin = l_balloon * nums[i] * r_balloon + backtrack(l, i - 1) + backtrack(i + 1, r)
                max_coin = max(max_coin, coin)
            cache[(l, r)] = max_coin
            return max_coin

        return backtrack(1, len(nums) - 2)

# TLE O(N!)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        cache = {}

        def backtrack(nums):
            if len(nums) == 0:
                return 0
            nums_tuple = tuple(nums)
            if nums_tuple in cache:
                return cache[nums_tuple]
            max_point = 0
            for i in range(len(nums)):
                l = nums[i - 1] if i - 1 >= 0 else 1
                r = nums[i + 1] if i + 1 < len(nums) else 1
                removed = nums.pop(i)
                p = l * removed * r
                max_point = max(max_point, p + backtrack(nums))
                nums.insert(i, removed)
            cache[nums_tuple] = max_point
            return cache[nums_tuple]
                
        return backtrack(nums)
