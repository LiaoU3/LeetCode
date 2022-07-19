class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> hm;
        int length = 0;
        for(int i=0; i<words.size(); i++){
            string word = words[i];
            string target = word;
            reverse(target.begin(), target.end());
            if(hm.count(target)&&hm[target]>0){
                hm[target]--;
                length += 4;
            }else{
                hm[word]++;
            }
        }
        for(auto it: hm){
            if(it.second>0 && it.first[0]==it.first[1]){
                length += 2;
                break;
            }
        }
        return length;
    }
};