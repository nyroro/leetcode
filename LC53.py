class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        ret = max(nums)
        if ret < 0:
            return ret
        now = nums[0]
        for i in xrange(1, len(nums)):
            if now > 0:
                now = now+nums[i]
            else:
                now = nums[i]
            ret = max(ret, now)
            print now
        return ret
            