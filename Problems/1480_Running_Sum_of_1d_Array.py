class Solution:
    def runningSum(self, nums: list) -> list:
        ret = []
        total = 0
        for num in nums:
            total += num
            ret.append(total)
        return ret