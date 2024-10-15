# Cleaner solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         res = []
#         pre_start = intervals[0][0]
#         pre_end = intervals[0][1]
#         for start, end in intervals:
#             if start <= pre_end:
#                 pre_end = max(pre_end, end)
#             else:
#                 res.append([pre_start, pre_end])
#                 pre_start = start
#                 pre_end = end
#         res.append([pre_start, pre_end])
#         return res