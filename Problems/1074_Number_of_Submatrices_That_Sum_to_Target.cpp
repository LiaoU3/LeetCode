
// got TLE at test case 39
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        vector<vector<int>> preSum(matrix.size(), vector<int>(matrix[0].size(), 0));
        int cnt = 0;
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<matrix[0].size(); j++){
                for(int r=i; r<matrix.size(); r++){
                    for(int c=j; c<matrix[0].size(); c++){
                        int up = r-1>=i ? preSum[r-1][c] : 0;
                        int left = c-1>=j ? preSum[r][c-1] : 0;
                        int upleft = r-1>=i && c-1>=j ? preSum[r-1][c-1] : 0;
                        preSum[r][c] = up+left-upleft+matrix[r][c];
                        if(preSum[r][c]==target) cnt++;
                    }
                }
            }
        }
        return cnt;
    }
};