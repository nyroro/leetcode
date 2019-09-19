import copy
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = copy.copy(nums)
        tmp = 0
        for i in xrange(len(self.sums)):
            self.sums[i]+=tmp
            tmp = self.sums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ret = self.sums[j]
        if i>0:
            ret -= self.sums[i-1]
        return ret
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)