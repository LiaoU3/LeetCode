class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> preSum;
        preSum[0] = 1;
        int cnt = 0;
        int currSum = 0;
        for(int i=0; i<nums.size(); i++){
            currSum += nums[i];
            cnt += preSum[currSum-k];
            preSum[currSum]++;
        }
        return cnt;
    }

};