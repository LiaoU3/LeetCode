#include <vector>

using namespace std;

// Time Complexity : O(N*Log(N))
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int m = nums.size();
        vector<int> dp(m, 0);
        int maxLen = 0;
        for (int i = 0; i < m; ++i) {
            int target = nums[i];
            int index = binarySearch(dp, target, 0, maxLen-1);
            if (index == maxLen) {
                dp[index] = nums[i];
                ++maxLen;
            } else {
                dp[index] = nums[i];
            }
        }
        return maxLen;
    }

    int binarySearch(vector<int>& dp, int target, int left, int right) {
        if (left > right) return left;
        int middle = (left + right) / 2;
        if (dp[middle] == target) {
            return middle;
        } else if (dp[middle] > target) {
            return binarySearch(dp, target, left, middle-1);
        } else {
            return binarySearch(dp, target, middle+1, right);
        }
    }
};


// Time Complexity : O(N**2)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int m = nums.size();
        vector<int> dp(m, 0);
        int maxLen = 0;
        for (int i = 0; i < m; ++i) {
            bool extend = true;
            for (int j = 0; j < maxLen; ++j) {
                if (nums[i] <= dp[j]) {
                    dp[j] = nums[i];
                    extend = false;
                    break;
                }
            }
            if (extend) {
                dp[maxLen] = nums[i];
                ++maxLen;
            }
        }   
        return maxLen;
    }
};