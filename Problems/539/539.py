class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timePoint in timePoints:
            time = 0
            time += int(timePoint.split(":")[0]) * 60
            time += int(timePoint.split(":")[1])
            times.append(time)

        times.sort()
        res = float("Inf")
        for i in range(len(times) - 1):
            res = min(res, times[i + 1] - times[i])
        print(times)
        res = min(res, 60 * 24 - times[-1] + times[0])
        return res
