class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x,y: x^y, nums)
        lowb = num&-num
        ret = [0, 0]
        for a in nums:
            if a & lowb == 0:
                ret[0] ^= a
            else:
                ret[1] ^= a
        return ret
        