class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zs = 0
        os = 0
        ts = 0
        for t in nums:
            if t==0:
                zs += 1
            elif t==1:
                os += 1
            else:
                ts+=1
        for i in xrange(zs):
            nums[i]=0
        for i in xrange(os):
            nums[zs+i]=1
        for i in xrange(ts):
            nums[zs+os+i]=2
        