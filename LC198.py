class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp = [[0]*2 for i in xrange(len(nums))]
        dp[0][1] = nums[0]
        for i in xrange(1,len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])
        