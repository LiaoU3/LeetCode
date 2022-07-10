class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> seenBiggest;
        seenBiggest.push({nums[0], 0});
        for(int i=1; i<nums.size(); i++){
            int maxValue = seenBiggest.top().first;
            int index = seenBiggest.top().second;
            while(index<i-k){
                seenBiggest.pop();
                maxValue = seenBiggest.top().first;
                index = seenBiggest.top().second;
            }
            nums[i] += maxValue;
            seenBiggest.push({nums[i], i});
        }
        return nums[nums.size()-1];
    }
};