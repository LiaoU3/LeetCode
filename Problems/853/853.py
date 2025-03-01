from typing import List
import heapq

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if target == 0:
            return 1

        time = [(target - p) / s for p, s in sorted(zip(position, speed))]
        print(time)
        # Monotonic increasiong
        stack = []
        for i in range(len(time) - 1, -1, -1):
            if not stack or time[i] > stack[-1]:
                stack.append(time[i])
        return len(stack)

# Use stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            stack.append([p, time])
        stack = sorted(stack)[::-1]
        res = 0
        pre_time = -1
        for _, time in stack:
            if time > pre_time:
                res += 1
                pre_time = time
        return res

# Use heap
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        heap = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            heapq.heappush(heap, [-p, -time])
        res = 0
        lead = -1
        while heap:
            _, time = heapq.heappop(heap)
            time = -time
            if time > lead:  # Cannot catch up with the front car
                res += 1
                lead = time
        return res
