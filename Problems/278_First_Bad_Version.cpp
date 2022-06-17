// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left  = 1;
        int right = n;
        int res   = 1;
        while(left<=right){
            int middle = (right-left)/2 + left;
            if(isBadVersion(middle)){
                res = middle;
                right = middle-1;
            }else{
                left = middle+1;
            }
        }
        return res;
    }
};