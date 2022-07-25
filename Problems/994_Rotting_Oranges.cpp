// Google Coding style
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int ROW = grid.size();
        int COL = grid[0].size();
        int step = 0;
        queue<pair<int, int>> qu;
        int freshCount = 0;
        for (int i = 0; i < ROW; ++i) {
            for (int j = 0; j < COL; ++j) {
                if (grid[i][j]==2) {
                    qu.push({i, j});
                }else if (grid[i][j] == 1) {
                    ++freshCount;
                }
            }
        }

        if (!freshCount) return step;

        while (!qu.empty()) {
            int len = qu.size();
            for(int i = 0; i < len; ++i){
                pair<int, int> coord = qu.front();
                qu.pop();
                int r = coord.first;
                int c = coord.second;
                for (pair<int, int> dir : directions) {
                    int nextr = r + dir.first;
                    int nextc = c + dir.second;
                    if (ROW>nextr && nextr>=0 && COL>nextc && nextc>=0){
                        if (grid[nextr][nextc] == 1) {
                            --freshCount;
                            grid[nextr][nextc] = 2;
                            qu.push({nextr, nextc});
                        }
                    }
                }
            }
            ++step;
        }
        if(freshCount){
            return -1;
        }else{
            return step-1;
        }
    }
};

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ROW = grid.size();
        int COL = grid[0].size();
        int fresh_cnt = 0;
        queue<pair<int, int>> qu;
        for(int r=0; r<ROW; r++){
            for(int c=0; c<COL; c++){
                if(grid[r][c]==2) qu.push({r, c});
                else if(grid[r][c]==1) fresh_cnt++;
            }
        }
        if(!fresh_cnt) return 0;
        vector<pair<int, int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int round_cnt = 0;
        while(!qu.empty()){
            round_cnt++;
            int qu_len = qu.size();
            for(int i=0; i<qu_len; i++){
                int r = qu.front().first;
                int c = qu.front().second;
                qu.pop();
                for(auto dir: directions){
                    int next_r = r+dir.first;
                    int next_c = c+dir.second;
                    if(ROW>next_r && next_r>=0 && COL>next_c && next_c>=0 && grid[next_r][next_c]==1){
                        grid[next_r][next_c] = 2;
                        fresh_cnt--;
                        qu.push({next_r, next_c});
                    }
                }
            }
        }
        if(fresh_cnt){
            return -1;
        }else{
            return round_cnt-1;
        }
    }
};