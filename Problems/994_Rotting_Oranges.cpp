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