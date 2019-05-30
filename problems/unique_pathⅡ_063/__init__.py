class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            elif obstacleGrid[0][i] == 0 and dp[0][i-1] != 1:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        for j in range(1, len(obstacleGrid)):
            if obstacleGrid[j][0] == 1:
                dp[j][0] = 0
            elif obstacleGrid[j][0] == 0 and dp[j-1][0] != 1:
                dp[j][0] = 0
            else:
                dp[j][0] = 1
        for m in range(1, len(obstacleGrid)):
            for n in range(1, len(obstacleGrid[0])):
                if obstacleGrid[m][n] == 1:
                    dp[m][n] = 0
                else:
                    dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
        return dp[-1][-1]
