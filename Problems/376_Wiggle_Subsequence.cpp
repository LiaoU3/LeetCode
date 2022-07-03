class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        dp[0] = 1;
        int state = 0;
        int curr = nums[0];
        for(int i=1; i<nums.size(); i++){
            int diff = nums[i]-curr;
            switch(state){
                case 0:
                    if(diff>0){
                        state = 1;
                        curr = nums[i];
                        dp[i] = dp[i-1]+1;
                    }else if(diff<0){
                        state = -1;
                        curr=  nums[i];
                        dp[i] = dp[i-1]+1;
                    }else{
                        dp[i] = dp[i-1];
                    }
                    break;
                case 1:
                    if(diff>0){
                        curr = nums[i];
                        dp[i] = dp[i-1];
                    }else if(diff<0){
                        state = -1;
                        curr = nums[i];
                        dp[i] = dp[i-1] + 1;
                    }else{
                        dp[i] = dp[i-1];
                    }
                    break;
                case -1:
                    if(diff>0){
                        state = 1;
                        curr = nums[i];
                        dp[i] = dp[i-1]+1;
                    }else if(diff<0){
                        curr = nums[i];
                        dp[i] = dp[i-1];
                    }else{
                        dp[i] = dp[i-1];
                    }
                    break;
            }
        }
        return dp[dp.size()-1];
    }
};