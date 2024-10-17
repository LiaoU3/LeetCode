class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int m = matrix.size();
        for (int i = 0; i < (m + 1) / 2; ++i) {
            for (int j = 0; j < m / 2; ++j) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[m-1-j][i];
                matrix[m-1-j][i] =  matrix[m-1-i][m-1-j];
                matrix[m-1-i][m-1-j] = matrix[j][m-1-i];
                matrix[j][m-1-i] = tmp;
            }
        }
    }
};