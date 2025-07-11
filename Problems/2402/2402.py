from heapq import heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        available = list(range(n))
        busy = []  # (end_time, room)

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(available, room)

            duration = end - start
            if available:
                room = heappop(available)
                heappush(busy, (start + duration, room))
            else:
                end_time, room = heappop(busy)
                heappush(busy, (end_time + duration, room))

            count[room] += 1

        return count.index(max(count))
