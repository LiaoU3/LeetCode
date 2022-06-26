#include<vector>
using namespace std;
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int curr_sum = 0;
        for(int i=0; i<k; i++){
            curr_sum += cardPoints[i];
        }
        int max_sum = curr_sum;
        for(int i=0; i<k; i++){
            curr_sum = curr_sum - cardPoints[k-i-1] + cardPoints[cardPoints.size()-i-1];
            max_sum = max(max_sum, curr_sum);
        }
        return max_sum;
    }
};