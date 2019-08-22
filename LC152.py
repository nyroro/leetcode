class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        t = nums[0]
        neg = nums[0]
        if neg >= 0:
            neg = 1
        if t<= 0:
            t = 1
        for i in xrange(1, len(nums)):
            t *= nums[i]
            neg *= nums[i]
            ret = max(t, ret)
            ret = max(neg, ret)
            tt = max(t, neg)
            nn = min(t, neg)
            if tt > 0:
                t = tt
            else:
                t = 1
            if nn < 0:
                neg = nn
            else:
                n = 1
            
        return ret
        
        