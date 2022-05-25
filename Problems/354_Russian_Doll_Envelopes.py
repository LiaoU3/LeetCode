# similar with problem 300 Longest Increasing Subsequence

from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        
        def binary_search_insert_index(ls, num):
            left = 0
            right = len(ls) - 1
            while left <= right:
                middle = (left + right) // 2
                if ls[middle]<num:
                    left = middle + 1
                elif ls[middle]>num:
                    right = middle - 1
                else:
                    return middle
            return left
        
        dp = []
        for _, width in envelopes:
            index = binary_search_insert_index(dp, width)
            if index == len(dp):
                dp.append(width)
            else:
                dp[index] = width
        return len(dp)