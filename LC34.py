class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)/2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid+1
        t_l = l
        if t_l>=len(nums) or t_l<0 or nums[t_l]!=target:
            return [-1,-1]
        l = t_l
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)/2
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        t_r = l-1
        return [t_l, t_r]
                
        