#include<vector>
#include<queue>
using namespace std;

// bfs
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int original_color = image[sr][sc];
        if(original_color==color) return image;
        queue<pair<int, int>> qu;
        vector<pair<int, int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        qu.push({sr, sc});
        image[sr][sc] = color;
        while(!qu.empty()){
            pair<int, int> curr = qu.front();
            int r = curr.first;
            int c = curr.second;
            qu.pop();
            for(auto dir: directions){
                int dr = dir.first;
                int dc = dir.second;
                int nxt_r = r+dr;
                int nxt_c = c+dc;
                if(image.size()>nxt_r && nxt_r>=0 && image[0].size()>nxt_c && nxt_c>=0 and image[nxt_r][nxt_c]==original_color){
                    image[nxt_r][nxt_c] = color;
                    qu.push({nxt_r, nxt_c});
                }
            }
        }
        return image;
    }
};
// dfs
// class Solution {
// public:
//     vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
//         int original_color = image[sr][sc];
//         if(original_color==color) return image;
//         dfs(image, sr, sc, color, original_color);
//         return image;
//     }
//     void dfs(vector<vector<int>>& image, int sr, int sc, int color, int original_color){
//         if(image[sr][sc]==original_color){
//             image[sr][sc] = color;
//             if(sr-1>=0)                 dfs(image, sr-1, sc, color, original_color);
//             if(image.size()>sr+1)       dfs(image, sr+1, sc, color, original_color);
//             if(sc-1>=0)                 dfs(image, sr, sc-1, color, original_color);
//             if(image[0].size()>=sc+1)   dfs(image, sr, sc+1, color, original_color);
//         }
//     }
// };