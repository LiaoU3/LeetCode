class Solution {
public:
int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    if(!maxMove) return 0;
	vector<vector<vector<int>>> dp (maxMove, vector<vector<int>>(m, vector<int>(n, 0)));
    int mod = 1000000007;
	// Intitialize
	for(int i=0; i<m; i++){
		dp[0][i][0]++;
		dp[0][i][n-1]++;
    }
    for(int i=0; i<n; i++){
        dp[0][0][i]++;
        dp[0][m-1][i]++;
    }
    int ans = dp[0][startRow][startColumn];
	for(int i=1; i<maxMove; i++){
		for(int j=0; j<m; j++){
			for(int k=0; k<n; k++){
				long up 	= j-1>=0 ? dp[i-1][j-1][k] : 0;
				int down	= m>j+1 ? dp[i-1][j+1][k] : 0;
				int left 	= k-1>=0 ? dp[i-1][j][k-1] : 0;
				int right 	= n>k+1 ? dp[i-1][j][k+1] : 0;
				dp[i][j][k] += (up + down + left + right)%mod;
            }
        }
        ans += dp[i][startRow][startColumn];
        ans %= mod;
	}
	return ans;
    // return ans;
}
};