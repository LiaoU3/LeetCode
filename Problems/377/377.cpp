#include <vector>
#include <climits>

using namespace std;

// we could use unsigned int to make it easier
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target+1, 0);
        dp[0] = 1;
        for (int i = 0; i < target + 1; ++i) {
            for (int num : nums) {
                if (i - num >= 0){
                    dp[i] += dp[i - num];
                }
            }
        }
        return dp[target];
    }
};

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<long long> dp(target+1, 0);
        dp[0] = 1;
        for (int i = 0; i < target + 1; ++i) {
            for (int num : nums) {
                if (i - num >= 0 and dp[i-num] != -1){
                    if (dp[i] + dp[i-num] > INT_MAX){
                        dp[i] = -1;
                        
                    }else{
                        dp[i] += dp[i - num];
                    }
                }
            }
        }
        return int(dp[target]);
    }
};