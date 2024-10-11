from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        times.sort()
        used_chairs = []  # leave, chair
        available_chairs = [i for i in range(len(times))]  # chair
        for arrival, leaving, i, in times:
            while used_chairs and used_chairs[0][0] <= arrival:
                _, used_chair = heappop(used_chairs)
                heappush(available_chairs, used_chair)
            available_chair = heappop(available_chairs)
            heappush(used_chairs, [leaving, available_chair])
            if i == targetFriend:
                return available_chair

# Wrong solution
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_time = times[targetFriend][0]
        res = 0
        for i, (arrival, leave) in enumerate(times):
            if i == targetFriend:
                continue
            if arrival <= target_time:
                res += 1
            if leave <= target_time:
                res -= 1
        return res


times = [[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
targetFriend = 6
s = Solution()
print(s.smallestChair(times, targetFriend))
