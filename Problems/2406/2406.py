class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = []  # minimum heap: right1, right2

        for l, r in intervals:
            if groups and groups[0] < l:
                group = heappop(groups)
            heappush(groups, r)
        return len(groups)
