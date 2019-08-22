from collections import Counter
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(m+1) for i in xrange(n+1)]
        dp[0][0]=1
        
        for t in strs:
            c = Counter(t)
            for i in xrange(n, c['1']-1,-1):
                for j in xrange(m, c['0'] - 1,-1):
                    # print i,j,i-c['1'],j-c['0'],dp[i-c['1']][j-c['0']]
                    if dp[i-c['1']][j-c['0']]>0:
                        # print i-c['1'],j-c['0']
                        dp[i][j] = max(dp[i-c['1']][j-c['0']]+1, dp[i][j])
            
            # print dp
        return max([max(t) for t in dp])-1