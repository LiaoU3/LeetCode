class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(), 1);
        for(int i=1; i<candies.size(); i++){
            if(ratings[i-1]<ratings[i]){
                candies[i] = candies[i-1]+1;
            }
        }
        for(int i=candies.size()-2; i>-1; i--){
            if(ratings[i]>ratings[i+1] && candies[i]<=candies[i+1]){
                candies[i] = candies[i+1]+1;
            }
        }
        int res = 0;
        for(int i=0; i<candies.size(); i++){
            res += candies[i];
        }
        return res;
    }
};