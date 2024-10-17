class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROW = matrix.size();
        int COL = matrix[0].size();
        int up = 0;
        int down = ROW-1;
        int middleR=0;
        while(up<=down){
            middleR = (up+down)/2;
            cout<<middleR<<endl;
            if(matrix[middleR][0]==target){
                return true;
            }else if(matrix[middleR][0]<target){
                up = middleR+1;
            }else{
                down = middleR-1;
            }
        }
        if(matrix[middleR][0]>target&&middleR>0){
            middleR--; 
        }

        int left = 0;
        int right = COL-1;
        int middleC=0;
        while(left<=right){
            int middleC = (left+right)/2;
            if(matrix[middleR][middleC]==target){
                return true;
            }else if(matrix[middleR][middleC]<target){
                left = middleC+1;
            }else{
                right = middleC-1;
            }
        }
        return false;
    }
};


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROW = matrix.size();
        int COL = matrix[0].size();
        int left = 0;
        int right = ROW*COL-1;
        while(left<=right){
            int middle = (left+right)/2;
            int r = middle/COL;
            int c = middle%COL;
            if(matrix[r][c]==target){
                return true;
            }else if(matrix[r][c]<target){
                left = middle+1;
            }else{
                right = middle-1;
            }
        }
        return false;
    }
};