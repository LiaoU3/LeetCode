#include<vector>
#include<numeric>
#include<algorithm>

using namespace std;

class Solution {
public:
    bool res = false;
    int avg;
    int N;
    bool makesquare(vector<int>& matchsticks) {
        int sum = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        if(sum%4)return false;
        avg = sum/4;
        N = matchsticks.size();
        sort(matchsticks.begin(), matchsticks.end(), [](int a, int b){return a>b;});
        dfs(matchsticks, 0, 0, 0, 0, 0);
        return res;
    }
    void dfs(vector<int>& matchsticks, int index, int len1, int len2, int len3, int len4){
        if(len1==avg && len2== avg && len3==avg && len4==avg){
            res = true;
            return;
        }
        if(res || index==N || len1>avg || len2>avg || len3>avg || len4>avg) return;
        dfs(matchsticks, index+1, len1+matchsticks[index], len2, len3, len4);
        if(index>0) dfs(matchsticks, index+1, len1, len2+matchsticks[index], len3, len4);
        if(index>1) dfs(matchsticks, index+1, len1, len2, len3+matchsticks[index], len4);
        if(index>2) dfs(matchsticks, index+1, len1, len2, len3, len4+matchsticks[index]);
    }
};