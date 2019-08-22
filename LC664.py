class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        dp = [[0]*len(s) for i in xrange(len(s))]
        for i in xrange(len(s)):
            dp[i][i] = 1
        for length in xrange(1, len(s)):
            for i in xrange(0, len(s)-length):
                dp[i][i+length] = dp[i][i] + dp[i+1][i+length]
                for k in xrange(1, length):
                    if s[i] == s[i+length] and s[i] == s[i+k]:
                        dp[i][i+length] = min(dp[i][i+length], dp[i][i+k]+dp[i+k+1][i+length]-1)
                    else:
                        dp[i][i+length] = min(dp[i][i+length], dp[i][i+k]+dp[i+k+1][i+length])
                    
                if s[i] == s[i+length]:
                    dp[i][i+length] = min(dp[i+1][i+length-1]+1, dp[i][i+length])
                    
        return dp[0][len(s)-1]
        