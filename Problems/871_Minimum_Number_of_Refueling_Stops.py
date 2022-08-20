from typing import List
import heapq

# greedy
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target == startFuel:
            return 0
        candidates = []
        currFuel = startFuel
        cnt = 0
        for distance, fuel in stations:
            if currFuel >= target:
                return cnt
            while currFuel < distance:
                if len(candidates) == 0:
                    break
                newFuel = -heapq.heappop(candidates)
                currFuel += newFuel
                cnt += 1
            if currFuel >= distance:
                heapq.heappush(candidates, -fuel)
            if len(candidates) == 0:
                break
        while currFuel < target:
            if not len(candidates):
                break
            newFuel = -heapq.heappop(candidates)
            currFuel += newFuel
            cnt += 1
        if currFuel >= target:
            return cnt
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    target = 1000
    startFuel = 299
    stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
    print(sol.minRefuelStops(target, startFuel, stations))