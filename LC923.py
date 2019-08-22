class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0]*(N+2) for i in xrange(K+2)]
        for i in xrange(N+1):
            dp[1][i] = i
            
        for i in xrange(2, K+1):
            for j in xrange(1, N+1):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] + 1
                
        for i in xrange(1,N+1):
            if dp[K][i]>=N:
                return i
        return N
        