#include<vector>
#include<queue>

using namespace std;

// bfs without using class
class Solution {
public:
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        for(int r=0; r<grid.size(); r++){
            for(int c=0; c<grid[0].size(); c++){
                max_area = max(max_area, bfs(grid, r, c));
            }
        }
        return max_area;
    }
    
    int bfs(vector<vector<int>> &grid, int r, int c){
        if(!grid[r][c]) return 0;
        queue<pair<int, int>> qu;
        qu.push({r, c});
        grid[r][c] = 0;
        int total=1;
        while(!qu.empty()){
            int curr_r = qu.front().first;
            int curr_c = qu.front().second;
            qu.pop();
            for(auto dir: directions){
                int nxt_r = curr_r + dir.first;
                int nxt_c = curr_c + dir.second;
                if(grid.size()>nxt_r && nxt_r>=0 && grid[0].size()>nxt_c && nxt_c>=0 && grid[nxt_r][nxt_c]){
                    qu.push({nxt_r, nxt_c});
                    grid[nxt_r][nxt_c] = 0; 
                    total++;
                }
            }
        }
        return total;
    }
};

// bfs
class Solution {
public:
    int curr_area = 0;
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        for(int r=0; r<grid.size(); r++){
            for(int c=0; c<grid[0].size(); c++){
                curr_area = 0;
                bfs(grid, r, c);
                max_area = max(max_area, curr_area);
            }
        }
        return max_area;
    }
    void bfs(vector<vector<int>> &grid, int r, int c){
        if(!grid[r][c]) return;
        curr_area++;
        queue<pair<int, int>> qu;
        qu.push({r, c});
        grid[r][c] = 0;
        while(!qu.empty()){
            int curr_r = qu.front().first;
            int curr_c = qu.front().second;
            qu.pop();
            for(auto dir: directions){
                int nxt_r = curr_r + dir.first;
                int nxt_c = curr_c + dir.second;
                if(grid.size()>nxt_r && nxt_r>=0 && grid[0].size()>nxt_c && nxt_c>=0 && grid[nxt_r][nxt_c]){
                    qu.push({nxt_r, nxt_c});
                    grid[nxt_r][nxt_c] = 0; 
                    curr_area++;
                }
            }
        }
    }
};

// dfs without using class parameters
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        for(int r=0; r<grid.size(); r++){
            for(int c=0; c<grid[0].size(); c++){
                maxArea = max(maxArea, dfs(r, c, grid));
            }
        }
        return maxArea;
    }
    int dfs(int r, int c, vector<vector<int>>& grid){
        if(r>=grid.size() || 0>r || c>=grid[0].size() || 0>c || !grid[r][c]) return 0;
        int total = 1;
        grid[r][c] = 0;
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for(auto dir: directions){
            total += dfs(r+dir.first, c+dir.second, grid);
        }
        return total;
    }
};

// dfs
// class Solution {
// public:
//     int curr_area = 0;
//     int maxAreaOfIsland(vector<vector<int>>& grid) {
//         int max_area = 0;
//         for(int r=0; r<grid.size(); r++){
//             for(int c=0; c<grid[0].size(); c++){
//                 curr_area = 0;
//                 dfs(grid, r, c);
//                 max_area = max(max_area, curr_area);
//             }
//         }
//         return max_area;
//     }

//     void dfs(vector<vector<int>>& grid, int r, int c){
//         if(grid[r][c]){
//             grid[r][c] = 0;
//             curr_area++;
//             if(r-1>=0)          dfs(grid, r-1, c);
//             if(grid.size()>r+1) dfs(grid, r+1, c);
//             if(c-1>=0)          dfs(grid, r, c-1);
//             if(grid[0].size()>c+1) dfs(grid, r, c+1);
//         }
//     }
// };