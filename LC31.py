class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        sep = -1
        for i in xrange(len(nums)-1):
            if nums[i]<nums[i+1]:
                sep = i
        print sep,nums[sep]
        if sep == -1:
            nums[::1] = nums[::-1]
            return
            
        t = sep+1
        for j in xrange(sep+1, len(nums)):
            if nums[j]>nums[sep]:
                t = j
        k = nums[t]
        nums[t] = nums[sep]
        nums[sep] = k
        nums[sep+1:len(nums)] = nums[sep+1:len(nums)][::-1]
        