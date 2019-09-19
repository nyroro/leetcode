class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<r:
            if l == r-1:
                return min(nums[l], nums[r])
            mid = (l+r)/2
            if nums[r]>nums[l]:
                return nums[l]
            elif nums[l]<nums[mid]:
                l = mid
            else:
                r = mid
        return nums[l]