#include <vector>
#include <unordered_map>
#include <algorithm>
#include <math.h>

using namespace std;
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        unordered_map<int, long long> dp;
        long long total = 0;
        long long mod = pow(10, 9) + 7;
        for (int i = 0; i < arr.size(); ++i) {
            int father = arr[i];
            dp[father] = 1;
            for (int j = 0; j < i; ++j) {
                int child = arr[j];
                if (child > sqrt(father)) break;
                if (father % child || dp.count(father/child) == 0) continue;
                long long tmp;
                if (child == father / child){
                    tmp = dp[child] * dp[child] % mod;
                }else{
                    tmp = dp[child] * dp[father/child] * 2 % mod;
                }
                tmp += dp[father];
                tmp %= mod;
                dp[father] = tmp;
            }
            total += dp[father];
            total %= mod;
        }
        return (int)total;
    }
};