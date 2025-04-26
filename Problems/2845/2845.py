class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1

        res = 0
        prefix = 0
        for num in nums:
            is_interesting = 1 if num % modulo == k else 0
            prefix += is_interesting
            res += counter[(prefix - k) % modulo]
            counter[prefix % modulo] += 1

        return res
