class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)/2
            print l,r,mid
            if target == nums[mid]:
                return mid
            elif target<nums[mid]:
                r=mid-1
            else:
                l = mid+1
        return -1
        