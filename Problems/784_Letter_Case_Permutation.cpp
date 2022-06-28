#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    vector<string> res;
    int LEN;
    string S;
    vector<string> letterCasePermutation(string s) {
        LEN = s.length();
        S = s;
        helper("", -1);
        return res;
    }
    void helper(string curr_string, int curr_index){
        if(curr_index == LEN-1){
            res.push_back(curr_string);
            return;
        }
        curr_index += 1;
        if(isalpha(S[curr_index])){
            string temp(curr_string);
            temp+=tolower(S[curr_index]);
            helper(temp, curr_index);
            temp = curr_string;
            temp += toupper(S[curr_index]);
            helper(temp, curr_index);
        }else{
            helper(curr_string+S[curr_index], curr_index);
        }
    }
};