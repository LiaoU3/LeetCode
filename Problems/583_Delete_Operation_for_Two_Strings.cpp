#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1 = size(word1);
        int len2 = size(word2);
        vector<vector<int>> dp (len1+1, vector<int>(len2+1, 0));

        for(int i=1; i<=len1; i++){
            for(int j=1; j<=len2; j++){
                if(word1[i-1] == word2[j-1]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return len1 + len2 - 2*dp[len1][len2];
    }
};