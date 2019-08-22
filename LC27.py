class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(nums)):
            if nums[i] == val:
                cnt+=1
            elif i-cnt>=0:
                nums[i-cnt] = nums[i]
        ret = len(nums)-cnt
        nums[:]=nums[:ret]
        return ret
        