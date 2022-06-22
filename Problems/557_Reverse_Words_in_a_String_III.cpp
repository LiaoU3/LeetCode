#include<string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int start = 0;
        int end = 0;
        string res;
        for(int i=0; i<s.length(); i++){
            if(s[i]==' '){
                end = i;
                for(int j=i-1; j>=start; j--){
                    res += s[j];
                }
                res+=' ';
                start = i+1;
            }
        }
        for(int j=s.length()-1; j>= start; j--){
            res += s[j];
        }
        return res;
    }
};