#include<vector>
#include<math.h>

using namespace std;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left  = 0;
        int right = nums.size()-1;
        int index = nums.size()-1;

        vector<int> res(nums.size(), 0);
        while(left<=right){
            if(abs(nums[left]) > abs(nums[right])){
                res[index] = pow(nums[left], 2);
                ++left;
            }else{
                res[index] = pow(nums[right], 2);
                --right;
            }
            --index;
        }
        return res;
    }
};