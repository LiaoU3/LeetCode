#include<iostream>
#include<string>

using namespace std;

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