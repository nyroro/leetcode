class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0]*(k+1) for i in xrange(n+1)]
        mod=int(1e9+7)
        dp[1][0] = 1
        for i in xrange(2,n+1):
            dp[i][0] = 1
            for j in xrange(1,k+1):
                dp[i-1][j] += dp[i-1][j-1]
                dp[i-1][j]%=mod
                dp[i][j] = dp[i-1][j]
                if j>=i:
                    dp[i][j]+=mod-dp[i-1][j-i]
                    dp[i][j]%=mod
        # print dp
        return dp[n][k]