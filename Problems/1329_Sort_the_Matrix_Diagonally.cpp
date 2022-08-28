#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        unordered_map<int, priority_queue<int, vector<int>, greater<int> > > hm;
        int m = mat.size();
        int n = mat[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                hm[i-j].push(mat[i][j]);
            }
        }
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                mat[i][j] = hm[i-j].top();
                hm[i-j].pop();
            }
        }
        return mat;
    }
};