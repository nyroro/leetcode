class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return True
        if len(nums)==1:
            return False
        s = sum(nums)
        if s%2==1:return False
        dp = [False]*(s/2+1)
        dp[0] = True
        
        for t in nums:
            for i in xrange(s/2,t-1, -1):
                dp[i] |= dp[i-t]
        return dp[s/2]