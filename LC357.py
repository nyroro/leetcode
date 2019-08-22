class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        dp = [[0]*2 for i in xrange(n+1)]
        dp[1][0]=1
        dp[1][1]=9
        for i in xrange(2,n+1):
            dp[i][0]=dp[i-1][0]+dp[i-1][1]
            dp[i][1]=dp[i-1][1]*(10-i+1)
        return dp[n][0]+dp[n][1]