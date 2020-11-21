class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p)+1) for i in range(len(s)+1)]
        
        dp[0][0] = True
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]
                    if i==0:
                        continue
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                        dp[i][j] |= dp[i-1][j-1]
                        dp[i][j] |= dp[i-1][j-2]
                elif i > 0 and s[i-1] == p[j-1]:
                    dp[i][j] |= dp[i-1][j-1]
                elif i > 0 and p[j-1] == '.':
                    dp[i][j] |= dp[i-1][j-1]
        return dp[len(s)][len(p)]
                    