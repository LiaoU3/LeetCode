#include <vector>
#include<queue>

using namespace std;
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> pac(m, vector<int>(n, 0));
        vector<vector<int>> atl(m, vector<int>(n, 0));
        queue<pair<int, int>> qu;
        for(int i = 0; i < m; ++i){
            pac[i][0] = 1;
            qu.push({i, 0});
        }
        for(int i = 1; i < n; ++i){
            pac[0][i] = 1;
            qu.push({0, i});
        }
        
        while(!qu.empty()){
            int len = qu.size();
            pair<int, int> coord = qu.front();
            qu.pop();
            int r = coord.first;
            int c = coord.second;
            for(pair<int, int> dir: directions){
                int nextr = r + dir.first;
                int nextc = c + dir.second;
                if(m > nextr && nextr >= 0 && n > nextc && nextc >= 0 && !pac[nextr][nextc] && heights[nextr][nextc] >= heights[r][c]){
                    pac[nextr][nextc] = 1;
                    qu.push({nextr, nextc});
                }
            }
        }

        for(int i = 0; i < m; ++i){
            atl[i][n-1] = 1;
            qu.push({i, n-1});
        }

        for(int i = 0; i < n-1; ++i){
            atl[m-1][i] = 1;
            qu.push({m-1, i});
        }
        while(!qu.empty()){
            int len = qu.size();
            pair<int, int> coord = qu.front();
            qu.pop();
            int r = coord.first;
            int c = coord.second;
            for(pair<int, int> dir: directions){
                int nextr = r + dir.first;
                int nextc = c + dir.second;
                if(m > nextr && nextr >= 0 && n > nextc && nextc >= 0 && !atl[nextr][nextc] && heights[nextr][nextc] >= heights[r][c]){
                    atl[nextr][nextc] = 1;
                    qu.push({nextr, nextc});
                }
            }
        }

        vector<vector<int>> res;
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                if(pac[i][j] && atl[i][j])
                    res.push_back({i, j});
            }
        }
        return res;
    }
};




// MLE
// class Solution {
// public:
//     vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
//         vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
//         int m = heights.size();
//         int n = heights[0].size();
//         vector<vector<int>> res;
//         for (int i = 0; i < m; ++i) {
//             for (int j = 0; j < n; ++j) {
//                 queue<pair<int, int>> qu;
//                 qu.push({i, j});
//                 bool reachPacific = false;
//                 bool reachAtlantic = false;
//                 vector<vector<int>> heightsCopy = {heights.begin(), heights.end()};
//                 while (!qu.empty()) {
//                     int len = qu.size();
//                     for(int k = 0; k < len; ++k) {
//                         pair<int, int> coord = qu.front();
//                         qu.pop();
//                         int r = coord.first;
//                         int c = coord.second;
//                         if (r == 0 || c == 0)
//                             reachPacific = true;
//                         if (r == m-1 || c == n-1)
//                             reachAtlantic = true;
//                         for (pair<int, int> dir : directions) {
//                             int nextr = r + dir.first;
//                             int nextc = c + dir.second;
//                             if (m > nextr && nextr >= 0 && n > nextc && nextc >= 0 && heightsCopy[r][c] >= heightsCopy[nextr][nextc]){
//                                 if (heightsCopy[nextr][nextc] == -1)
//                                     continue;
//                                 if (nextr == 0 || nextc == 0) {
//                                     reachPacific = true;
//                                 }else if (nextr == m-1 || nextc == n-1){
//                                     reachAtlantic = true;
//                                 }
//                                 if (reachPacific && reachAtlantic)
//                                     break;
//                                 qu.push({nextr, nextc});

//                             }
//                         }
//                         if (reachPacific && reachAtlantic)
//                             break;
//                         heightsCopy[r][c] = -1;
//                     }
//                     if (reachPacific && reachAtlantic)
//                         break;
//                 }
//                 if (reachPacific && reachAtlantic)
//                     res.push_back({i, j});
//                 // break;
//             }
//             // break;
//         }
//         return res;
//     }
// };

int main(){
    vector<vector<int>> heights = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
    Solution sol;
    sol.pacificAtlantic(heights);
    return 0;
}