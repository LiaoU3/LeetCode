class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int pivot = 0;
        int leftSum = 0;
        int rightSum = 0;
        for(int i=1; i< nums.size(); i++){
            rightSum += nums[i];
        }
        if(leftSum==rightSum) return 0;
        while(pivot<nums.size()-1){
            leftSum  += nums[pivot];
            rightSum -= nums[pivot+1];
            pivot++;
            if(leftSum==rightSum) return pivot;
        }
        return -1;
    }
};