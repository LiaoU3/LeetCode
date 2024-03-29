class NumArray {
public:
    vector<int> v;
    int sumUp=0;
    NumArray(vector<int>& nums) {
        v = nums;
        for (int i = 0; i < nums.size(); ++i) {
            sumUp += nums[i];
        }
    }
    
    void update(int index, int val) {
        sumUp += val - v[index];
        v[index] = val;
    }
    
    int sumRange(int left, int right) {
        if (right - left > v.size() / 2) {
            int res = sumUp;
            for (int i = 0; i<left; ++i) {
                res -= v[i];
            }
            for (int i = right + 1; i < v.size(); ++i) {
                res -= v[i];
            }
            return res;
        }else{
            int res = 0;
            for (int i = left; i < right + 1; ++i) {
                res += v[i];
            }
            return res;
        }
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */