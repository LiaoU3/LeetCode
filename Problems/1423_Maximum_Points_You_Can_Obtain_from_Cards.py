from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_sum = max_sum = sum(cardPoints[:k])
        for i in range(k):
            curr_sum = curr_sum - cardPoints[k-i-1] + cardPoints[-i-1]
            max_sum = max(max_sum, curr_sum)
        return max_sum