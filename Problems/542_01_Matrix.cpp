#include<vector>
#include<queue>

using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int ROW = mat.size();
        int COL = mat[0].size();
        vector<vector<int>> dist(ROW, vector<int>(COL, __INT_MAX__));
        queue<pair<int, int>> qu;
        for(int r=0; r<ROW; r++){
            for(int c=0; c<COL; c++){
                if(mat[r][c]==0){
                    dist[r][c] = 0;
                    qu.push({r, c});
                }
            }
        }
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        while(!qu.empty()){
            int curr_r = qu.front().first;
            int curr_c = qu.front().second;
            qu.pop();
            for(auto dir: directions){
                int nxt_r = curr_r + dir.first;
                int nxt_c = curr_c + dir.second;
                if(ROW>nxt_r && nxt_r>=0 && COL>nxt_c && nxt_c>=0 && dist[nxt_r][nxt_c]>dist[curr_r][curr_c]+1){
                    dist[nxt_r][nxt_c] = dist[curr_r][curr_c]+1;
                    qu.push({nxt_r, nxt_c});
                }
            }
        }
        return dist;
    }
};