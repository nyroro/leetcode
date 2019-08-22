class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        now = 0
        if len(nums)==1:
            return True
        for i in xrange(len(nums)):
            if i<=now:
                now = max(i+nums[i], now)
                if now >= len(nums)-1:
                    return True
        return False
        