class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = []
        for i in range(n+1):
            dp.append(0)
        dp[1] = 1
        dp[2] = 2
        if n >= 3:
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]