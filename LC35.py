import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if target<=nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)/2
            if nums[mid]<=target:
                l = mid
            else:
                r = mid
            if l == r-1:
                print target, nums[l], nums[r]
                if nums[r]==target:
                    return r
                if nums[r]<target:
                    return r+1
                
                if nums[l] == target:
                    return l
                if nums[l]<target:
                    return l+1
        return l
        