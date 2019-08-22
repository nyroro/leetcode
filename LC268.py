class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        T = (1+len(nums))*(len(nums))/2
        return T-S
        