class Solution {
public:
    vector<vector<int>> res;
    int MAX_LEN;
    vector<int> nums_;
    vector<vector<int>> permute(vector<int>& nums) {
        MAX_LEN = nums.size();
        nums_ = nums;
        vector<int> tmp1;
        vector<int> tmp2;
        helper(tmp1, tmp2);
        return res;
    }
    void helper(vector<int>& curr_list, vector<int>& histort_index_list){
        if(curr_list.size()==MAX_LEN) res.push_back(curr_list);
        for(int i=0; i<MAX_LEN; i++){
            if(find(histort_index_list.begin(), histort_index_list.end(), i)!=histort_index_list.end()) continue;
            vector<int> tmp1 = curr_list;
            tmp1.push_back(nums_[i]);
            vector<int> tmp2(histort_index_list);
            tmp2.push_back(i);
            helper(tmp1, tmp2);
        }
    }
};