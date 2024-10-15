from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1  = buy2  = -float('Inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1  = max(buy1, -p)
            sell1 = max(sell1, p + buy1)
            buy2  = max(buy2, -p + sell1)
            sell2 = max(sell2, p + buy2)
        return sell2

# Cannot buy and sell at the same time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        hp = [0, 0]
        for i in range(1, len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            else:
                heappush(hp, prices[i] - smallest)
                heappop(hp)
        return sum(hp)

if __name__ =='__main__':
    sol = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(sol.maxProfit(prices))