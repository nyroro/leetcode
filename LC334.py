class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        num1 = 0x7fffffff
        num2 = 0x7fffffff
        for i in xrange(len(nums)):
            if nums[i]<=num1:
                num1 = nums[i]
            elif nums[i]<=num2:
                num2 = nums[i]
            else:
                return True
        return False
            