#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> tmp;
        traverse(candidates, target, res, tmp, 0);
        return res;
    }
    
    void traverse(vector<int>& candidates, int target, vector<vector<int>> &res, vector<int> cand, int curr) {
        int sum = 0;
        for (int i = 0; i < cand.size(); ++i)
            sum += cand[i];
        if (sum == target){
            res.push_back(cand);
            return;
        }
        if (sum > target)
            return;
        
        for (int i = curr; i < candidates.size(); ++i) {
            vector<int> tmp (cand);
            tmp.push_back(candidates[i]);
            traverse(candidates, target, res, tmp, i);
        }
    }
};