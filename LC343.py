class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None]*59
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        if n<=3:
            return dp[n]
        for i in xrange(4,n+1):
            dp[i] = 0
            for j in xrange(1,i):
                dp[i] = max(dp[i], (i-j)*j)
                dp[i] = max(dp[i], dp[i-j]*j)
                dp[i] = max(dp[i], (i-j)*dp[j])
                dp[i] = max(dp[i], dp[i-j]*dp[j])
        return dp[n]