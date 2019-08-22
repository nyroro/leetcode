class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0xfffffff]*(len(nums))
        dp[0] = 0
        last = 1
        for i in xrange(0, len(nums)):
            tmp_start = last
            tmp_last = min(i+nums[i],len(nums)-1)
            last = max(last, tmp_last)
            
            for j in xrange(tmp_start, tmp_last+1):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[len(nums)-1]
            
                
        