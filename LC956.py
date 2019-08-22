class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        dp = [[0]*(L+1) for i in xrange(N+1)]
        dp[0][0] = 1
        
        for j in xrange(1, L+1):
            for i in xrange(1, N+1):
                if j<i:
                    continue
                dp[i][j] += dp[i-1][j-1]*(N-i+1)
                if j<=K:
                    if i<j-1:continue
                    dp[i][j] += dp[i][j-1]*(i-j+1)
                else:
                    if i<K:continue
                    dp[i][j] += dp[i][j-1]*(i-K)
                dp[i][j]%=int(1e9+7)
        return dp[N][L]