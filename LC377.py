class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1)
        dp[0] = 1
        for i in xrange(1,target+1):
            for t in nums:
                if i-t>=0:
                    dp[i]+=dp[i-t]
        return dp[target]
        