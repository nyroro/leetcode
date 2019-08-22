import copy
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        table = {}
        ret = 0
        k1 = len(nums)/2
        k2 = len(nums)-k1
        
        for t in xrange(1<<k1):
            s = 0
            for j in xrange(k1):
                if t&(1<<j) == 0:
                    s+=nums[j]
                else:
                    s-=nums[j]
            table[S-s] = table.get(S-s,0)+1
        
        for t in xrange(1<<k2):
            s = 0
            for j in xrange(k2):
                if t&(1<<j) == 0:
                    s+=nums[k1+j]
                else:
                    s-=nums[k1+j]
            ret+=table.get(s,0)
        return ret
                