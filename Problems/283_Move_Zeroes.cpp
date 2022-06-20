#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int point_non_zero = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]){
                swap(nums[i], nums[point_non_zero]);
                point_non_zero++;
            }
        }
    }
};

// class Solution {
// public:
//     void moveZeroes(vector<int>& nums) {
//         int point = 0;
//         for(auto num:nums){
//             if(num){
//                 nums[point] = num;
//                 point++;
//             }
//         }
//         for(; point<nums.size(); point++){
//             nums[point] = 0;
//         }
//     }
// };