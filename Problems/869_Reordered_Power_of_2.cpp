class Solution {
public:
    bool reorderedPowerOf2(int n) {
        vector<char> v1;
        string s1 = to_string(n);
        for (auto c : s1) {
            v1.push_back(c);
        }
        sort(v1.begin(), v1.end());
        
        for (int i = 0; i < 31; ++i) {
            int target = pow(2, i);
            string s2 = to_string(target);
            vector<char> v2;
            for (auto c : s2) {
                v2.push_back(c);
            }
            if (v2.size() > v1.size()) {
                break;
            }
            sort(v2.begin(), v2.end());
            if (v1 == v2) return true;
        }
        return false;
    }
};