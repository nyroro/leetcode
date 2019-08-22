import copy
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0]*10
        dpn = [1]*10
        
        N -= 1
        for i in xrange(N):
            dp = copy.copy(dpn)
            dpn[0] = dp[4] + dp[6]
            
            dpn[1] = dp[8] + dp[6]
            dpn[2] = dp[7] + dp[9]
            dpn[3] = dp[4] + dp[8]
            dpn[4] = dp[3] + dp[9] + dp[0]
            dpn[5] = 0
            dpn[6] = dp[1] + dp[7] + dp[0]
            dpn[7] = dp[2] + dp[6]
            dpn[8] = dp[1] + dp[3]
            dpn[9] = dp[4] + dp[2]
            for j in xrange(len(dpn)):
                dpn[j]%=(10**9+7)
        return sum(dpn)%(10**9+7)
            