class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> table(26, 0);
        int maxCount = 0;
        int maxLen = 0;
        int l = 0;
        for(int r=0; r<s.length(); r++){
            table[s[r]-'A']++;
            maxCount = max(maxCount, table[s[r]-'A']);
            while(r-l+1-maxCount>k){
                table[s[l]-'A']--;
                l++;
            }
            maxLen = max(maxLen, r-l+1);
        }
        return maxLen;
    }
};