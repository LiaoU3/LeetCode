class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        if(len1>len2) return findMedianSortedArrays(nums2, nums1);
        if(!len1) return ((double)nums2[(len2-1)/2]+nums2[len2/2])/2;
        int left1 = 0;
        int right1 = len1;
        int middle1;
        int middle2;
        while(left1<=right1){
            middle1 = (left1+right1)/2;
            middle2 = (len1+len2+1)/2-middle1;
            double l1 = middle1==0? INT_MIN : nums1[middle1-1];
            double l2 = middle2==0? INT_MIN : nums2[middle2-1];
            double r1 = middle1==len1? INT_MAX : nums1[middle1];
            double r2 = middle2==len2? INT_MAX : nums2[middle2];
            if(l1<=r2 && l2<=r1){
                if((len1+len2)%2){
                    return max(l1, l2);
                }else{
                    return (max(l1, l2) + min(r1, r2))/2;
                }
            }
            else if(l1>r2) right1 = middle1-1;
            else left1 = middle1+1;
        }
        return -1;
    }

};