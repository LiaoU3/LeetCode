#include<iostream>
#include<vector>
#include<set>

using namespace std;
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int curr_sum = 0;
        int max_sum  = 0;
        int left = 0;
        set<int> seen;

        for(auto num:nums){
            while(seen.count(num)){
                seen.erase(nums[left]);
                curr_sum -= nums[left];
                left++;
            }
            seen.insert(num);
            curr_sum += num;
            max_sum = max(max_sum, curr_sum);
        }
        return max_sum;
    }
};