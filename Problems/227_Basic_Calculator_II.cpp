#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    int calculate(string s) {
        vector<int> stack;
        char operand = '+';
        int curr_num = 0;
        for(int i=0; i<s.length(); i++){
            if(isdigit(s[i])){
                curr_num = curr_num*10 - '0'+ s[i];
            }
            if (s[i]=='+' || s[i]=='-' || s[i]=='*' || s[i]=='/'|| i==s.length()-1){
                if(operand=='+'){
                    stack.push_back(curr_num);
                }else if(operand=='-'){
                    stack.push_back(-curr_num);
                }else if(operand=='*'){
                    stack[stack.size()-1] *= curr_num;
                }else{
                    stack[stack.size()-1] /= curr_num;
                }
                operand = s[i];
                curr_num = 0;
            }   
        }
        int total = 0;
        for (auto num:stack){
            total += num;
        }
        return total;
    }
};
int main(){
    string s = "2147483647";
    Solution sol;
    cout <<sol.calculate(s)<<endl;
}