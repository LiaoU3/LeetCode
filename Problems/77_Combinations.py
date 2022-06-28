from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(curr_ls: List[int], curr_num: int):
            if len(curr_ls) == k:
                res.append(curr_ls)
            for i in range(curr_num+1, n+1):
                helper(curr_ls + [i], i)
        helper([], 0)
        return res
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         def helper(curr_ls):
#             if len(curr_ls)== k:
#                 res.append(curr_ls)
#             for i in range(curr_ls[-1]+1, n+1):
#                 helper(curr_ls+[i])
        
#         for i in range(1, n+1):
#             helper([i])
#         return res