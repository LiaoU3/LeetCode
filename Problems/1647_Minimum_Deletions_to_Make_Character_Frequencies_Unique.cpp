#include<string>
#include<vector>
#include<set>
#include<algorithm>

using namespace std;

class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq_table(26, 0);
        for(auto c: s){
            freq_table[c-'a']++;
        }
        sort(freq_table.begin(), freq_table.end(), greater<int>());
        set<int> freq_set;
        int delete_cnt = 0;
        for(auto freq: freq_table){
            if(!freq) break;
            while(freq_set.count(freq)){
                freq--;
                delete_cnt++;
            }
            if(freq) freq_set.insert(freq);
        }
        return delete_cnt;
    }
};