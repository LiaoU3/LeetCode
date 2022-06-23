import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        heap = []
        heapq.heapify(heap)

        curr_days = 0
        for duration, deadline in courses:
            if curr_days + duration <= deadline:
                curr_days += duration
                heapq.heappush(heap, -duration)
            else:
                poped = heapq.heappushpop(heap, -duration)
                curr_days = curr_days + poped + duration
        return len(heap)

if __name__ == '__main__':
    sol = Solution()
    courses = [[1,2],[2,3]]
    print(sol.scheduleCourse(courses))