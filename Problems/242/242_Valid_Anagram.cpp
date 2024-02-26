// using only one vector
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        
        vector<int> table(26, 0);
        for (char c : s) {
            ++table[c - 'a'];
        }
        for (char c : t) {
            --table[c - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (table[i]) return false;
        }
        return true;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        
        vector<int> sTable(26, 0);
        vector<int> tTable(26, 0);
        for (char c : s) {
            ++sTable[c - 'a'];
        }
        for (char c : t) {
            ++tTable[c - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (sTable[i] != tTable[i]) return false;
        }
        return true;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        
        vector<int> sTable(26, 0);
        vector<int> tTable(26, 0);
        for (int i = 0; i < s.size(); ++i) {
            ++sTable[s[i] - 'a'];
        }
        for (int i = 0; i < t.size(); ++i) {
            ++tTable[t[i] - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (sTable[i] != tTable[i]) return false;
        }
        return true;
    }
};