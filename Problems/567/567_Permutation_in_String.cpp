#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.length()>s2.length()) return false;
        vector<int> alpha_table_1(26, 0);
        vector<int> alpha_table_2(26, 0);
        for(auto c: s1) alpha_table_1[c-'a']++;
        for(int i=0; i<s1.size(); i++) alpha_table_2[s2[i]-'a']++;
        if(alpha_table_1==alpha_table_2) return true;
        for(int i=s1.length(); i<s2.length(); i++){
            alpha_table_2[s2[i]-'a']++;
            alpha_table_2[s2[i-s1.length()]-'a']--;
            if(alpha_table_1==alpha_table_2) return true;
        }
        return false;
    }
};