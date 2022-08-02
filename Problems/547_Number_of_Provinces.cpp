class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]){
                traverse(i, visited, isConnected);
                ++cnt;
            }
        }
        return cnt;
    }
    
    void traverse(int i, vector<bool> &visited, vector<vector<int>>& isConnected) {
        visited[i] = true;
        for (int j = 0; j < visited.size(); ++j) {
            if (isConnected[i][j] && !visited[j])
                traverse(j, visited, isConnected);
        }
    }
};