class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [[0]*len(nums) for i in xrange(len(nums))]
        sums = [0]
        for t in nums:
            sums.append(sums[-1]+t)
        for i in xrange(len(nums)):
            dp[i][i] = nums[i]
            
        for i in xrange(1,len(nums)):
            for j in xrange(0,len(nums)):
                l = j
                r = j+i
                if r>=len(nums):
                    break
                lval = nums[l]+sums[r+1]-sums[l]-dp[l+1][r]
                rval = nums[r]+sums[r+1]-sums[l]-dp[l][r-1]
                dp[l][r] = max(lval, rval)
        return dp[0][len(nums)-1]>=sums[len(nums)]/2
            