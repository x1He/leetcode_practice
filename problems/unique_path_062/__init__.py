class Solution:
    def uniquePaths(self, m, n):
        if m < n:
            m,n = n,m
        dp = [1 for i in range(m)]

        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[-1]
