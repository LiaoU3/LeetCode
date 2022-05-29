class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]

if __name__ =='__main__':
    sol = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(sol.change(amount, coins))