class Solution:
    def minPathSum(self, grid):
        dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for m in range(1, len(grid)):
            for n in range(1, len(grid[0])):
                dp[m][n] = min(dp[m-1][n], dp[m][n-1]) + grid[m][n]
        return dp[-1][-1]


if __name__ == '__main__':
    m = [[1,3,1],[1,5,1],[4,2,1]]
    dp = Solution().minPathSum(m)
    print(dp)