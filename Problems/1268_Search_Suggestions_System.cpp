#include<vector>
#include<string>
#include<iostream>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> res;
        vector<string> curr = products;

        for(int i=0; i<searchWord.length(); ++i){
            vector<string> nxt;
            for(auto word: curr){
                if(i<word.length() && searchWord[i]==word[i]){
                    nxt.push_back(word);
                }
            }
            curr = nxt;
            vector<string> three;
            for(int i=0; i<curr.size(); ++i){
                three.push_back(curr[i]);
                if(i==2){
                    break;
                }
            }
            res.push_back(three);
        }
        return res;
    }
};