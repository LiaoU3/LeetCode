class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res

# TLE Time complexity: O(n ** 2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        h = []  # (-gas, index)
        for i, g in enumerate(gas):
            heappush(h, (-g, i))
        while h:
            g, i = heappop(h)
            g = -g
            total = 0
            for j in range(i, len(gas)):
                total += gas[j]
                total -= cost[j]
                if total < 0:
                    break
            else: 
                for j in range(i):
                    total += gas[j]
                    total -= cost[j]
                    if total < 0:
                        break
                else:
                    return i
        return -1