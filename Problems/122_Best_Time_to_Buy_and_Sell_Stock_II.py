from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        pre_price = prices[0]
        for price in prices[1:]:
            if pre_price<price:
                total += price-pre_price
            pre_price = price
        return total