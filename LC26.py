class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0 
        for i in xrange(len(nums)):
            if i == 0:
                continue
            if nums[i]==nums[i-1]:
                cnt +=1
            nums[i-cnt]=nums[i]
        ret = len(nums)-cnt
        # print ret
        nums[:]=nums[:ret]
        return ret
        