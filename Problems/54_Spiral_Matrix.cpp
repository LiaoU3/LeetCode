class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int ROW = matrix.size();
        int COL = matrix[0].size();
        int cnt = ROW*COL-1;
        int r = 0;
        int c = 0;
        res.push_back(matrix[0][0]);
        matrix[0][0] = 101;

        while(1){
            while(c+1<COL && matrix[r][c+1]!=101){
                c++;
                cnt--;
                res.push_back(matrix[r][c]);
                matrix[r][c] = 101;
                if(!cnt)break;
            }
            if(!cnt)break;

            while(r+1<ROW && matrix[r+1][c]!=101){
                r++;
                cnt --;
                res.push_back(matrix[r][c]);
                matrix[r][c] = 101;
                if(!cnt)break;
            }
            if(!cnt)break;
            while(c-1>=0 && matrix[r][c-1]!=101){
                c--;
                cnt --;
                res.push_back(matrix[r][c]);
                matrix[r][c] = 101;
                if(!cnt)break;
            }
            if(!cnt)break;
            while(r-1>=0 && matrix[r-1][c]!=101){
                r--;
                cnt--;
                res.push_back(matrix[r][c]);
                matrix[r][c] = 101;
                if(!cnt)break;
            }
            if(!cnt)break;
        }
        return res;
    }
};