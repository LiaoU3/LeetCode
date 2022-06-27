class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(c) for c in n)
# class Solution:
#     def minPartitions(self, n: str) -> int:
#         max_num = 0
#         for c in n:
#             max_num = max(max_num, int(c))
#         return max_num