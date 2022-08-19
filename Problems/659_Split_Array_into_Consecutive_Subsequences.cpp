class Solution {
public:
    bool isPossible(vector<int>& nums) {
        // key : number, val : count
        map<int, int> hm;
        for (auto num : nums) {
            ++hm[num];
        }
        for (auto && it : hm) {
            int num = it.first;
            while (it.second > 0) {
                int len = 0;
                int currCnt = 0;
                int j = num;
                while (hm[j] >= currCnt) {
                    currCnt = hm[j];
                    --hm[j];
                    ++len;
                    ++j;
                }
                if (len < 3) return false;
            }
        }
        return true;
    }
};