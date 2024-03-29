class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (!amount) return 0;
        vector<int> dp(amount+1, -1);
        dp[0] = 0;
        for (int i = 1; i < amount + 1; ++i) {
            for (auto coin : coins) {
                if (i - coin >= 0) {
                    if (dp[i - coin] != -1) {
                        if (dp[i] == -1) {
                            dp[i] = dp[i - coin] + 1;
                        }else{
                            dp[i] = min(dp[i], dp[i - coin] + 1);
                        }
                    }
                }
            }
        }
        return dp[amount];
    }
};