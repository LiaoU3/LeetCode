class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> hm;
        for (auto c : s) {
            ++hm[c];
        }
        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (hm[c] == 1) return i;
        }
        return -1;
    }
};