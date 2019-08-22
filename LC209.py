class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sums = [0]*(length+1)
        for i in xrange(length):
            sums[i+1] = nums[i]
            sums[i+1] += sums[i]
        if sums[length]<s:
            return 0
        ret = length
        
        i = 0
        j = 1
        while j<=length:
            while j<=length and sums[j] - sums[i] < s:
                j+=1
            ret = min(j-i, ret)
            if j>length:
                break
            while i<j and sums[j]-sums[i]>=s:
                ret = min(j-i, ret)
                i+=1
        return ret
        