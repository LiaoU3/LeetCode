class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end());
        vector<vector<int>> qu(people.size(), {-1, -1});
        for(auto man: people){
            int height = man[0];
            int infront = man[1];
            int cnt = 0;
            for(int i=0; i<qu.size(); i++){
                if(cnt==infront && qu[i][0]==-1){
                    qu[i] = man;
                    break;
                }else if(qu[i][0]==-1 || qu[i][0]==height) cnt++;

            }
        }
        return qu;
    }
};