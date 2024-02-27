#include<vector>
#include<unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> table;
        vector<int> res;
        for(int i=0; i<nums.size(); i++){
            if(table.count(nums[i])){
                res.push_back(table[nums[i]]);
                res.push_back(i);
                return res;
            }
            table[target-nums[i]] = i;
        }
        return res;
    }
};