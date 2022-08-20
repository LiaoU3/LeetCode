#include<iostream>
#include<string>

using namespace std;

// using set makes it faster
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (!s.length()) return 0;
        unordered_set<char> seen;
        int l = 0;
        int maxLen = 1;
        for (int r = 0; r < s.length(); ++r) {
            while (seen.count(s[r])) {
                seen.erase(s[l]);
                ++l;
            }
            seen.insert(s[r]);
            maxLen = max(maxLen, r - l + 1);
        }
        return maxLen;
    }
};

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.size();
        int lastSeen[95];
        for (int i = 0; i < 95; ++i)
            lastSeen[i] = -1;
        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < s.length(); ++right){
            left = max(left, lastSeen[s[right]-32]+1);
            maxLen = max(maxLen, right-left+1);
            lastSeen[s[right]-32] = right;
        }
        return maxLen;
    }
};

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len = 0;
        string sub_string;
        for(auto c: s){
            while(sub_string.find(c) != string::npos){
                sub_string.erase(0, 1);
            }
            sub_string += c;
            max_len = max<int>(max_len, sub_string.length());
        }
        return max_len;
    }
};

int main(){
    Solution sol;
    string s =  "abcabcbb";
    cout <<sol.lengthOfLongestSubstring(s)<<endl;
    return 0;
}