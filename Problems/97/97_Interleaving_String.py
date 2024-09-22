class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    continue
                c = s3[i + j - 1]
                # look up
                if i - 1 >= 0 and dp[i - 1][j] and c == s2[i - 1]:
                    dp[i][j] = True
                # look left
                if j - 1 >= 0 and dp[i][j - 1] and c == s1[j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        dp[0][0] = True
        
        for i in range(1,  len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        
        for i in range(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s2[i-1]==s3[i-1] 
            
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]