#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int maxLen = 1;
        int start  = 0;
        for(int i=0; i<s.length(); ++i){
            if(i-maxLen>=1){
                bool flag = false;
                string sub1(s.substr(i-maxLen-1, maxLen+2));
                string sub2(sub1.rbegin(), sub1.rend());
                if(sub1==sub2){
                    start = i-maxLen-1;
                    maxLen += 2;
                    flag = true;
                }
                if (flag){
                    continue;
                }
            }
            if(i-maxLen>=0){
                string sub1(s.substr(i-maxLen, maxLen+1));
                string sub2(sub1.rbegin(), sub1.rend());
                if(sub1==sub2){
                    start = i-maxLen;
                    maxLen += 1;
                }
            }
        }
        return s.substr(start, maxLen);
    }
};

int main(){
    string s = "cbbd";
    Solution sol;
    cout << sol.longestPalindrome(s);
    return 0;
}