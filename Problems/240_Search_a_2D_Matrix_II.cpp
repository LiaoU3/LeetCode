class Solution {
public:
bool searchMatrix(vector<vector<int>>& matrix, int target) {
	int ROW = matrix.size();
	int COL = matrix[0].size();
	int i = 0;
	int j = COL-1;
	while(ROW>i && i>=0 && COL>j && j>=0){
		if(matrix[i][j]==target)
			return true;
		if(matrix[i][j]>target){
			j--;
		}else{
			i++;
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
        int right = COL-1;
        int middleC;
        while(left<=right){
            middleC= (left+right)/2;
            if(matrix[0][middleC]==target)
                return true;
            if(matrix[0][middleC]<target){
                left = middleC+1;
            }else{
                right = middleC-1;
            }
        }
        if(matrix[0][middleC]>target && middleC!=0)
            middleC--;

        int up = 0;
        int down = ROW-1;
        int middleR;
        while(up<=down){
            middleR = (up+down)/2;
            if(matrix[middleR][0]==target)
                return true;
            if(matrix[middleR][0]<target){
                up = middleR+1;
            }else{
                down = middleR-1;
            }
        }
        if(matrix[middleR][0]>target && middleR!=0)
            middleR--;
        
        for(int i=0; i<=middleR; i++){
            int l = 0;
            int r = middleC;
            while(l<=r){
                int m = (l+r)/2;
                if(matrix[i][m]==target)
                    return true;
                if(matrix[i][m]<target){
                    l = m+1;
                }else{
                    r = m-1;
                }
            }
        }
        return false;
    }
};

// TLE
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROW = matrix.size();
        int COL = matrix[0].size();

        int left = 0;
        int right = COL-1;
        int middleC;
        while(left<=right){
            middleC= (left+right)/2;
            if(matrix[0][middleC]==target)
                return true;
            if(matrix[0][middleC]<target){
                left = middleC+1;
            }else{
                right = middleC-1;
            }
        }
        if(matrix[0][middleC]>target && middleC!=0)
            middleC--;

        int up = 0;
        int down = ROW-1;
        int middleR;
        while(up<=down){
            middleR = (up+down)/2;
            if(matrix[middleR][0]==target)
                return true;
            if(matrix[middleR][0]<target){
                up = middleR+1;
            }else{
                down = middleR-1;
            }
        }
        if(matrix[middleR][0]>target && middleR!=0)
            middleR--;
        
        for(int i=0; i<=middleR; i++){
            for(int j=0; j<=middleC; j++){
                if(matrix[i][j]==target)
                    return true;
                if(matrix[i][j]>target)
                    break;
            }
        }
        return false;
    }
};


