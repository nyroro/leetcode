class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 10*18
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l<r:
            print l,r
            if l==r-1:
                if nums[l]<=nums[r]:
                    return nums[l]
                else:
                    return nums[r]
            mid = (l+r)/2
            if nums[r]>nums[l]:
                return nums[l]
            elif nums[r]<nums[l]:
                if nums[mid]<nums[r]:
                    r=mid
                elif nums[mid]>nums[r]:
                    l = mid
                else:
                    r = mid
            else:
                return min(self.findMin(nums[l:mid]), self.findMin(nums[mid:r+1]))
                    
        