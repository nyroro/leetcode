class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        now = 0
        
        for t in nums:
            if t == 1:
                now += 1
            else:
                now = 0
            ret = max(ret, now)
        return ret