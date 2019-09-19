class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = grid[0]
        for i in xrange(1,len(grid[0])):
            dp[i]+=dp[i-1]
        for i in xrange(1, len(grid)):
            dp[0]+=grid[i][0]
            for j in xrange(1, len(grid[i])):
                dp[j] = min(dp[j-1], dp[j])+grid[i][j]
        return dp[len(dp)-1]