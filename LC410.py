class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        sums = [None]*len(nums)
        sums[0] = nums[0]
        for i in xrange(1, len(nums)):
            sums[i] = nums[i]+sums[i-1]
        
        dp = [[0xffffffff]*len(nums) for i in xrange(m)]
        for i in xrange(len(nums)):
            dp[0][i] = sums[i]
        for i in xrange(1,m):
            for j in xrange(0, len(nums)-1):
                for k in xrange(j, len(nums)):
                    dp[i][k] = min(dp[i][k], max(dp[i-1][j],sums[k]-sums[j]))
        return dp[m-1][len(nums)-1]