#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        for(int i=0; i<words.size(); i++){
            string word_rev(words[i].rbegin(), words[i].rend());   
            words[i] = word_rev;
        }
        sort(words.begin(), words.end());
        words.erase(unique(words.begin(), words.end()), words.end());

        int length =  1;
        string pre_word = "";
        for(auto word: words){
            if (word.find(pre_word) != 0){
                length += pre_word.length()+1;
            }
            pre_word = word;
        }

        return length + words[words.size()-1].length();
    }
};