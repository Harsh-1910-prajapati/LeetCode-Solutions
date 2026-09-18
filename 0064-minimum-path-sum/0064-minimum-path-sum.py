class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [float('inf')] * (n + 1)
        dp[1] = 0

        for i in range(m):
            for j in range(1, n + 1):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j - 1]

        return dp[n]