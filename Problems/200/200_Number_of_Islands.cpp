// dfs
class Solution {
public:
    vector<vector<char>> Grid;
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int ROW, COL;
    int numIslands(vector<vector<char>>& grid) {
        Grid = grid;
        ROW = grid.size();
        COL = grid[0].size();
        int cnt = 0;
        for(int r=0; r<ROW; r++){
            for(int c=0; c<COL; c++){
                if (Grid[r][c]=='1'){
                    cnt ++;
                    dfs(r, c);
                }
            }
        }
        return cnt;
    }
    void dfs(int r, int c){
        if(!(ROW>r && r>=0 && COL>c && c>=0 && Grid[r][c]=='1')) return;
        Grid[r][c] = '0';
        for(auto dir: directions){
            int nr = r+dir.first;
            int nc = c+dir.second;
            dfs(nr, nc);
        }
    }
};
// bfs
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ROW=grid.size();
        int COL=grid[0].size();
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int cnt = 0;
        for(int r=0; r<ROW; r++){
            for(int c=0; c<COL; c++){
                if(grid[r][c]=='1'){
                    cnt++;
                    queue<pair<int, int>> qu;
                    qu.push({r, c});
                    while(!qu.empty()){
                        int cr = qu.front().first;
                        int cc = qu.front().second;
                        qu.pop();
                        for(auto dir: directions){
                            int nr = cr+dir.first;
                            int nc = cc+dir.second;
                            if(ROW>nr && nr>=0 && COL>nc && nc>=0 && grid[nr][nc]=='1'){
                                grid[nr][nc] = '0';
                                qu.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }
        return cnt;
    }

};