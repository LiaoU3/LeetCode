#include<string>
#include<stack>
#include<iostream>

using namespace std;
class Solution {
public:
    string decodeString(string s) {
        stack<char> stck;
        for(char c: s){
            if(c!=']') stck.push(c);
            else{
                string str = "";
                while(stck.top()!='['){
                    str = stck.top()+str;
                    stck.pop();
                }
                stck.pop();
                string num = "";
                while(!stck.empty() && isdigit(stck.top())){
                    num = stck.top()+num;
                    stck.pop();
                }
                for(int i=0; i<stoi(num); i++){
                    for(int j=0; j<str.length(); j++){
                        stck.push(str[j]);
                    }
                }
            }
        }
        string ans = "";
        while(!stck.empty()){
            ans = stck.top()+ans;
            stck.pop();
        }
        return ans;
    }
};

int main(){
    string s = "3[a]2[bc]";
    Solution sol;
    string ans = sol.decodeString(s);
    cout<<ans<<endl;
    return 0;
}