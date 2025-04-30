class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def has_even_digits(num):
            cnt = 0
            while num:
                cnt += 1
                num //= 10
            return cnt % 2 == 0

        res = 0
        for num in nums:
            if has_even_digits(num):
                res += 1
        return res
