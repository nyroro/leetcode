class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        length = len(nums)
        dp = [[[0] * 4 for i in xrange(length)] for j in xrange(length+1)]
        
        for i in xrange(length-1):
            # 左右两端都不偷
            dp[2][i][0] = 0
            dp[2][i][1] = nums[i]
            dp[2][i][2] = nums[i+1]
            dp[2][i][3] = 0
            
        for i in xrange(3, length+1):
            # 长度为i
            for j in xrange(0, length-i+1):
                dp[i][j][0] = max([dp[i-1][j][2], dp[i-1][j+1][1], dp[i-2][j+1][3]])
                # 偷左端不偷右端
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][3])
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j+1][0]+nums[j])
                
                # 偷右端不偷左端
                dp[i][j][2] = max(dp[i-1][j+1][2], dp[i-1][j+1][3])
                dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][0]+nums[j+i-1])
                
                # 两端都偷
                dp[i][j][3] = max(dp[i-1][j][1]+nums[j+i-1],nums[j]+dp[i-1][j+1][2])
                
        return max([dp[length][0][1], dp[length][0][2], dp[length][0][0]])
            
        
        