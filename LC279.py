import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in xrange(2, n+1):
            t = int(math.sqrt(i))
            if t*t == i:
                dp[i] = 1
                continue
            
            dp[i] = min(dp[i-j*j] for j in xrange(1, t+1)) + 1
        return dp[n]