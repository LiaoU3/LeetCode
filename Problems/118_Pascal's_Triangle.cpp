#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        ans.push_back(vector<int>{1});

        for(int i=1; i<numRows;i++){
            vector<int> new_row;
            new_row.push_back(1);
            for(int j=0; j<ans[ans.size()-1].size()-1; j++){
                new_row.push_back(ans[ans.size()-1][j] + ans[ans.size()-1][j+1]);
            }
            new_row.push_back(1);
            ans.push_back(new_row);
        }
        return ans;
    }
};

int main(){
    Solution sol;
    int numRows = 5;
    sol.generate(numRows);
}