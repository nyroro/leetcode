class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = {t:set() for t in stones}
        dp[0] = {1}
        for i in xrange(0, len(stones)-1):
            for v in dp[stones[i]]:
                if stones[i]+v in dp:
                    if v-1>0:
                        dp[stones[i]+v].add(v-1)
                    dp[stones[i]+v].add(v)
                    dp[stones[i]+v].add(v+1)
        return len(dp[stones[-1]])>0
        
        