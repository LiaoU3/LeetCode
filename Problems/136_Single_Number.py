# Why do I use XOR ?
# Let’s assume the input is [4,1,2,1,2]
# So the representation in binary would be
# [4, 0100
# 1,  0001
# 2,  0010
# 1,  0001
# 2   0010]

# Let’s see if we do the XOR on 1 and 1
# 0001
# 0001
# It will make them to 0000

# Because the XOR would make the same numbers to 0(0000), which means the paired numbers are gonna disappear anyway, and we will get the only single number in the end.

# Then you think : but we are not doing it on 1 and 1 but 4 and 1.
# There’s no difference at all, cause we are gonna do it on 1 ( paired numbers ) eventually.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans