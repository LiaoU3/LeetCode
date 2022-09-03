class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> res;
        for (int i = 1; i < 10; ++i) {
            helper(n, k, res, i, 1);
        }
        return res;
    }
    void helper(int n, int k, vector<int> &res, int num, int digit) {
        if (digit == n) {
            res.push_back(num);
            return;
        }
        int tailNum = num % 10;
        int tmp = num;
        if (tailNum + k < 10) {
            tmp *= 10;
            tmp += tailNum + k;
            helper(n, k, res, tmp, digit + 1);
        }
        if (!k) return;
        tmp = num;
        if (tailNum - k >= 0) {
            tmp *= 10;
            tmp += tailNum - k; 
            helper(n, k, res, tmp, digit + 1);
        }
    }
};