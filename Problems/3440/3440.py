from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)

        leftMax = [0] * N
        currMax = 0
        prev = 0
        for i in range(N):
            leftMax[i] = currMax
            currMax = max(currMax, startTime[i] - prev)
            prev = endTime[i]

        rightMax = [0] * N
        currMax = 0
        prev = eventTime
        for i in range(N - 1, -1, -1):
            rightMax[i] = currMax
            currMax = max(currMax, prev - endTime[i])
            prev = startTime[i]

        res = 0
        for i, (start, end) in enumerate(zip(startTime, endTime)):
            interval = end - start
            left_bound = 0 if i == 0 else endTime[i - 1]
            right_bound = eventTime if i == N - 1 else startTime[i + 1]
            res = max(res, right_bound - left_bound - interval)
            if leftMax[i] >= interval or rightMax[i] >= interval:
                res = max(res, right_bound - left_bound)

        return res
