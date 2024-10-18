class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, target, 0, nums.size()-1);
    }
    int binarySearch(vector<int>& nums, int target, int left, int right){
        if(left>right)
            return -1;
        int middle = (left+right)/2;
        if(nums[middle]==target)
            return middle;
        
        // left ascending
        if(nums[left]<=nums[middle]){
            if(nums[left]<=target && target<nums[middle])
                return binarySearch(nums, target, left, middle-1);
            else
                return binarySearch(nums, target, middle+1, right);
        // right ascending
        }else{
            if(nums[middle]<target && target<=nums[right])
                return binarySearch(nums, target, middle+1, right);
            else
                return binarySearch(nums, target, left, middle-1);
        }
        return -1;
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        while(left<=right){
            int middle = (left+right)/2;
            cout<<middle<<endl;
            if(nums[middle]==target){
                return middle;
                
            // left normal ascending
            }else if(nums[left]<=nums[middle]){
                if(nums[left]<=target && target<nums[middle]){
                    right = middle-1;
                }else{
                    left = middle+1;
                }
            
            // right normal ascendind
            }else{
                if(nums[middle]<target && target<=nums[right]){
                    left = middle+1;
                }else{
                    right = middle-1;
                }
            }
        }
        return -1;
    }
};