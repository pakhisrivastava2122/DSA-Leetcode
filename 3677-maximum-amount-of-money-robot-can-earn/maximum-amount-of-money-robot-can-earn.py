from math import inf

class Solution:
    def maximumAmount(self, grid):
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][k]: max money at (i,j) using k skips
        dp = [[[-inf]*3 for _ in range(n)] for _ in range(m)]
        
        # Start position
        dp[0][0][0] = grid[0][0]
        dp[0][0][1] = 0  # skip
        dp[0][0][2] = 0  # skip
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue
                    
                    val = grid[i][j]
                    
                    # From top
                    if i > 0:
                        # take
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                        # skip
                        if k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                    
                    # From left
                    if j > 0:
                        # take
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                        # skip
                        if k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        
        return max(dp[m-1][n-1])