#include<vector>
#include<math.h>

using namespace std;

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int pre_pre = -pow(10, 5);
        int pre     = -pow(10, 5);
        int curr    = -pow(10, 5);
        int count   = 0;
        for(auto num:nums){
            pre_pre = pre;
            pre     = curr;
            curr    = num;
            if(pre>curr){
                count ++;
                if(count==2){
                    return false;
                }
                if(pre_pre>curr){
                    curr = pre;
                }
            }
        }
        return true;
    }
};