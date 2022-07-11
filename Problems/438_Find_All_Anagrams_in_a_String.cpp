#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        int lenS = s.length();
        int lenP = p.length();
        if(lenS<lenP) return res;

        vector<int> alphaS(26, 0);
        for(int i=0; i<lenP; i++) alphaS[s[i]-'a']++;

        vector<int>alphaP(26, 0);
        for(auto c: p) alphaP[c-'a']++;

        if(alphaS==alphaP) res.push_back(0);
        for(int i=1; i<lenS-lenP+1; i++){
            alphaS[s[i-1]-'a'] --;
            alphaS[s[i-1+lenP]-'a'] ++;
            if(alphaS==alphaP) res.push_back(i);
        }
        return res;
    }
};