class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = strs[0];
        int i = 0;
        for(int i=0; i<strs[0].length(); i++){
            for(int j=1; j<strs.size(); j++){
                if(strs[j][i] != strs[0][i]) return res.substr(0, i);
            }
        }
        return res;
    }
};