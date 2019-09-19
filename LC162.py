class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        l = 0
        r = len(nums)-1
        if nums[l]>nums[l+1]:
            return l
        if nums[r]>nums[r-1]:
            return r
        while l<r:
            mid = (l+r)/2
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l