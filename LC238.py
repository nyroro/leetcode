class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1]*len(nums)
        # left
        acc = nums[0]
        for i in xrange(1,len(nums)):
            ret[i] = acc
            acc*=nums[i]
        acc = nums[-1]
        for i in xrange(len(nums)-2, -1, -1):
            ret[i] *= acc
            acc *= nums[i]
        return ret
        