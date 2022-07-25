#include<vector>
using namespace std;
//Time Complexity: O(log(n))
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>res;
        if (!nums.size()) {
            res.push_back(-1);
            res.push_back(-1);
            return res;
        }
        
        int left = 0;
        int right = nums.size()-1;
        int middle;
        bool found = false;
        while (left<=right) {
            middle = (left+right)/2;
            if (nums[middle]>=target) {
                if(nums[middle]==target)
                    found = true;
                right = middle-1;
            } else {
                left = middle+1;
            }
        }
        if (!found) {
            res.push_back(-1);
            res.push_back(-1);
            return res;
        }
        int l = right+1;

        left = l;
        right = nums.size()-1;
        while (left<=right) {
            middle = (left+right)/2;
            if (nums[middle]<=target) {
                left = middle+1;
            } else {
                right = middle-1;
            }
        }
        int r = left-1;
        res.push_back(l);
        res.push_back(r);
        return res;
    }
};

// Time Complexity O(n)
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        vector<int>res;
        for(; left<nums.size(); left++){
            if(nums[left]==target){
                res.push_back(left);
                break;
            }

        }
        if(left==nums.size()){
            res.push_back(-1);
            res.push_back(-1);
                return res;
        }

        for(; left<=right; right--){
            if(nums[right]==target){
                res.push_back(right);
                break;
            }
        }
        return res;
    }
};