class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int ROW = matrix.size();
        int COL = matrix[0].size();
        for(int r=0; r<ROW; r++){
            for(int c=1; c<COL; c++){
                matrix[r][c] += matrix[r][c-1];
            }
        }
        int cnt = 0;
        for(int cl=0; cl<COL; cl++){
            for(int cr = cl; cr<COL; cr++){
                unordered_map<int, int> hm;
                hm[0] = 1;
                int curr = 0;
                for(int r=0; r<ROW; r++){
                    curr += matrix[r][cr]-(cl>0 ? matrix[r][cl-1] : 0);
                    cnt += hm[curr-target];
                    hm[curr]++;
                }		
            }
        }
        return cnt;
    }
};

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