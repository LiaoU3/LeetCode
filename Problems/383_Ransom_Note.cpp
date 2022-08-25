class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) return false;
        unordered_map<char, int> hm;
        for (auto c : magazine) {
            ++hm[c];
        }
        for (auto c : ransomNote) {
            if (--hm[c] < 0) return false;
        }
        return true;
    }
};

// using two map
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) return false;
        unordered_map<char, int> hm1;
        unordered_map<char, int> hm2;
        for (auto c : ransomNote) {
            ++hm1[c];
        }
        for (auto c : magazine) {
            ++hm2[c];
        }
        for (auto it = hm1.begin(); it != hm2.end(); ++it) {
            char key = it -> first;
            if (it -> second > hm2[key]) {
                return false;
            }
        }
        return true;
    }
};

// using two map
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) return false;
        unordered_map<char, int> hm1;
        unordered_map<char, int> hm2;
        for (auto c : ransomNote) {
            ++hm1[c];
        }
        for (auto c : magazine) {
            ++hm2[c];
        }
        for (auto it : hm1) {
            char key = it.first;
            if (it.second > hm2[key]) {
                return false;
            }
        }
        return true;
    }
};