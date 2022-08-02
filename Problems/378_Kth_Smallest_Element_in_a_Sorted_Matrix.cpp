class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> hp;
        int n = matrix.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                hp.push(matrix[i][j]);
                if (hp.size()>k)
                    hp.pop();
            }
        }
        return hp.top();
    }
};