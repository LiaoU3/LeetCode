class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.length()!=t.length()) return false;
        vector<int> sMap(127, -1);
        vector<int> tMap(127, -1);
        for(int i=0; i<s.length(); i++){
            if(sMap[s[i]] != -1){
                if(tMap[t[i]]!=s[i]) return false;
                // sMap[s[i]] = t[i];
                // tMap[t[i]] = s[i];
            }else{
                if(tMap[t[i]]!=-1) return false;
                sMap[s[i]] = t[i];
                tMap[t[i]] = s[i];
            }
        }
        return true;
    }
};