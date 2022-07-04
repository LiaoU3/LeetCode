class Solution {
public:
    int longestPalindrome(string s) {
        vector<int> alphaCountTable(58, 0);
        for(auto c: s){
            alphaCountTable[c-'A']++;
        }
        int res = 0;
        bool haveOdd = false;
        for(auto cnt: alphaCountTable){
            if(cnt%2 == 1){
                haveOdd = true;
                res += cnt-1;
            }else{
                res += cnt;
            }
        }
        if(haveOdd)res++;
        return res;
    }
};