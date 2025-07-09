from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        curr = 0
        pre = 0
        res = 0
        for index in range(k):
            curr += endTime[index] - startTime[index]

        for index in range(k, len(startTime)):
            res = max(res, startTime[index] - pre - curr)
            curr -= (endTime[index - k] - startTime[index - k])
            curr += (endTime[index] - startTime[index])
            pre = endTime[index - k]

        res = max(res, eventTime - pre - curr)
        return res


k = 1
startTime = [1,3]
endTime = [2,5]
sol = Solution()
print(sol.maxFreeTime(endTime, k, startTime, endTime))
