class Solution {
public:
    bool isSubsequence(string s, string t) {
        int point = 0;
        for(int i=0; i<t.length(); i++){
            if(point==s.length()) return true;
            if(t[i]==s[point]){
                point++;
            }
        }
        return point==s.length();
    }
};