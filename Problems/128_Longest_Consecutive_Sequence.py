class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 1
        for num in numsSet:
            # which means it's the start of the sequence
            if num-1 not in numsSet:
                length = 1
                while num+1 in numsSet:
                    length += 1
                    longest = max(longest, length)
                    num += 1
        return longest if nums else 0