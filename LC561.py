class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ret = 0
        for i in xrange(0, len(nums),2):
            ret+=nums[i]
        return ret
        