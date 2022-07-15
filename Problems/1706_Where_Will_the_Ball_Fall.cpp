class Solution {
public:
vector<int> findBall(vector<vector<int>>& grid) {
    vector<int> res;
    for(int c = 0; c<grid[0].size(); c++){
            res.push_back(fall(grid, 0, c));
    }
    return res;
}
int fall(vector<vector<int>>& grid, int r, int c){
    if(r==grid.size()) return c;
    if(grid[r][c]==1){
        if(c+1==grid[0].size() || grid[r][c+1]==-1) return -1;
        return fall(grid, r+1, c+1);
    }else{
        if(c==00 || grid[r][c-1]==1) return -1;
        return fall(grid, r+1, c-1);
    }
}
};