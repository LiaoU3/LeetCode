class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxProduct = nums[0];
        int localMin = nums[0];
        int localMax = nums[0];
        
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < 0){
                int tmp;
                tmp = localMax;
                localMax = localMin;
                localMin = tmp;
            }
            localMax = max(nums[i], nums[i]*localMax);
            localMin = min(nums[i], nums[i]*localMin);
            maxProduct = max(maxProduct, localMax);
        }
        return maxProduct;
    }
};