class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            while nums[nums[i]-1] != nums[i]:
                t = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i]=t
                # for j in xrange(len(nums)):
                #     print nums[j],
                # print 
                
            
        ret = []
        for i in xrange(len(nums)):
            if nums[i]!=i+1:
                ret.append(i+1)
        return ret
        