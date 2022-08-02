#include<vector>
#include<algorithm>
#include<cstdlib>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int closest = 0;
        for (int i = 0; i < 3; ++i)
            closest += nums[i];
        
        for (int i = 0; i < nums.size(); ++i) {
            int l = i + 1;
            int r = nums.size()-1;
            while (l < r){
                int sumUp = nums[i] + nums[l] + nums[r];
                if (sumUp == target) {
                    return target;
                }else if (sumUp > target) {
                    --r;
                }else{
                    ++l;
                }
                if (abs(sumUp - target) < abs(closest - target))
                    closest = sumUp;
            }
        }
        return closest;
    }
};