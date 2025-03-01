class Solution {
public:
    string multiply(string num1, string num2) {
        string ans = "";
        if((num1.length()==1 && !(num1[0]-'0')) || (num2.length()==1 && !(num2[0]-'0'))) return "0";
        int tmpLen = num1.length()+num2.length();
        vector<int> tmp(tmpLen, 0);
        for(int i=num1.length()-1; i>=0; i--){
            for(int j=num2.length()-1; j>=0; j--){
                tmp[i+j+1] += (num1[i]-'0')*(num2[j]-'0');            
            }
        }
        for(int i=tmpLen-1; i>0; i--){
            tmp[i-1] += tmp[i]/10;
            tmp[i] %= 10;
            char c = tmp[i]+'0';
            ans = c + ans;
        }
        if(tmp[0]){
            ans = char(tmp[0]+'0') + ans;
        }
        return ans;
    }
};