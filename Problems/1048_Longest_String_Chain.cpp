#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), compareByLength);
        vector<int> lens;
        for(int k=0; k<words.size(); k++){
            int curr_len = 1;
            for(int i=0; i<(int)words[k].length(); i++){
                string temp = words[k].substr(0, i) + words[k].substr(i+1);
                for(int j=0; j<k; j++){
                    if (temp == words[j]){
                        curr_len = max(curr_len, lens[j]+1);
                    }
                }
            }
            lens.push_back(curr_len);
        }
        return *max_element(lens.begin(), lens.end());
    }

private:
    static bool compareByLength(string s1, string s2){
        return s1.length()<s2.length();
    }
};
int main(){
    return 0;
}