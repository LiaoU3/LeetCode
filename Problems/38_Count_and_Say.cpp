#include<iostream>
#include<string>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string ans = "1";
        for(int i=1; i<n; i++){
            char curr_num = ans[0];
            int count_curr_num = 1;
            string ans_next = "";
            for(int j=1; j<ans.length(); j++){
                if (ans[j] == curr_num){
                    count_curr_num++;
                }else{
                    ans_next = ans_next + to_string(count_curr_num) + curr_num;
                    count_curr_num = 1;
                    curr_num = ans[j];
                }
            }
            ans = ans_next + to_string(count_curr_num) + curr_num;
        }
        return ans;
    }
};