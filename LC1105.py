class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0]*len(B) for i in xrange(len(A))]
        for i in xrange(len(A)):
            
            for j in xrange(len(B)):
                if i>0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j>0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                if A[i]==B[j]:
                    if i>0 and j>0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                    else:
                        dp[i][j] = 1
        return dp[len(A)-1][len(B)-1]
                