#include<vector>
using namespace std;
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int length = nums.size();
        k %= length;
        if(!k){
            return;
        }

        int count = gcd(k, length);

        for(int i=0; i<count; i++){
            int curr_point = i+k;
            int pre_num = nums[i];
            while(curr_point != i){
                int temp = nums[curr_point];
                nums[curr_point] = pre_num;
                pre_num = temp;
                
                curr_point += k;
                curr_point %= length;
            }
            nums[i] = pre_num;
        }
        
    }
    int gcd(int m, int n){
        if(n==0){
            return m;
        }else{
            return gcd(n, m%n);
        }
    }
};
int main(){
    Solution sol;
    vector<int> nums = {1,2,3,4,5,6,7};
    int k = 3;
    sol.rotate(nums, k);
}