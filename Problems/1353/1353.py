class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        hp = []
        res = 0
        start = events[0][0]
        end = max(event[1] for event in events)
        i = 0
        for day in range(start, end + 1):
            while i < len(events) and events[i][0] <= day:
                heappush(hp, events[i][1])
                i += 1
            while hp and hp[0] < day:
                heappop(hp)
            if hp:
                heappop(hp)
                res += 1
        return res
