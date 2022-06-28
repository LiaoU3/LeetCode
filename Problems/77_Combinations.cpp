#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> res;
    int n_;
    int k_;
    vector<vector<int>> combine(int n, int k) {
        n_ = n;
        k_ = k;
        vector<int> temp;
        helper(temp, 0);
        return res;
    }
    void helper(vector<int> &curr_ls, int curr_num){
        if(curr_ls.size()==k_){
            res.push_back(curr_ls);
        }
        // cout<<curr_num<<endl;
        for(int i=curr_num+1; i<n_+1; i++){
            vector<int> tep_ls(curr_ls);
            tep_ls.push_back(i);
            helper(tep_ls, i);
        }
    }
};
int main(){
    Solution sol;
    int n=4;
    int k=2;
    sol.combine(n, k);
    return 0;
}