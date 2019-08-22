class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        for t in xrange(1<<(len(nums))):
            numset = []
            for i,k in enumerate(nums):
                if ((1<<i)&t)!=0:
                    numset.append(k)
            ret.append(numset)
        return ret
        