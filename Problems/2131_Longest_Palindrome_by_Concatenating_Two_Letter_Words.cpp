#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

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

class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> hm;
        for (string word : words) {
            ++hm[word];
        }
        int total = 0;
        int same = false;
        for (auto iter : hm) {
            string word = iter.first;
            int cnt1 = iter.second;
            string rev = word;
            reverse(rev.begin(), rev.end());
            if (word == rev) {
                total += (cnt1/2) * 4;
                if (cnt1 % 2)
                    same = true;
            }else {
                if (!hm.count(rev)) {
                    continue;	
                }
                int cnt2 = hm[rev];
                int used = min(cnt1, cnt2);
                total += used * 4;
                hm[word] -= used;
                hm[rev]  -= used;
            }
        }
        return same ? total + 2 : total;
    }
};