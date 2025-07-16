class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        all_even = 0  # prev -> even
        all_odd = 0  # prev -> odd
        even_odd = 0  # prev -> odd
        odd_even = 0  # prev -> even
        for num in nums:
            if num % 2 == 1:
                all_odd += 1
                even_odd = max(even_odd, odd_even + 1)
            else:
                all_even += 1
                odd_even = max(odd_even, even_odd + 1)
        return max(all_even, all_odd, even_odd, odd_even)
