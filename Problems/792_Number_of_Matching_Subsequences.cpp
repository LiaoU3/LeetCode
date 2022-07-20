class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        unordered_map<char, vector<int>> hm;
        for(int i=0; i<s.size(); i++){
            hm[s[i]].push_back(i);
        }
        int cnt = 0;
        for(int i=0; i<words.size(); i++){
            string word(words[i]);
            int pre = -1;
            cnt++;
            for(char c: word){
                if(hm.count(c)){
                    auto it = upper_bound(hm[c].begin(), hm[c].end(), pre);
                    if(it==hm[c].end()){
                        cnt--;
                        break;
                    }
                    pre = *it;
                }else{
                    cnt--;
                    break;
                }
            }
        }
        return cnt;
    }
};

// optimize using 2 set to restore every passed and failed word
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int cnt = 0;
        unordered_set<string> pass, fail;
        for(int i=0; i<words.size(); i++){
            string word(words[i]);
            if(pass.count(word)){
                cnt++;
                continue;
            }else if(fail.count(word)){
                continue;
            }
            int index = 0;
            for(int j=0; j<s.length();j++){
                if(word[index]==s[j]){
                    index++;
                    if(index==word.length())
                        break;
                }
            }
            if(index==word.length()){
                cnt++;
                pass.insert(word);
            }else{
                fail.insert(word);
            }
        }
        return cnt;
    }
};

// TLE
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int cnt = 0;
        for(int i=0; i<words.size(); i++){
            string word(words[i]);
            int index = 0;
            for(int j=0; j<s.length();j++){
                if(word[index]==s[j]){
                    index++;
                    if(index==word.length())
                        break;
                }
            }
            if(index==word.length())
                cnt++;
        }
        return cnt;
    }
};