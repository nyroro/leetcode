class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[mid]<=nums[r]:
                    if target <= nums[r]:
                        l = mid+1
                    else:
                        r = mid-1
                else:
                    l = mid+1
            else:
                # target<nums[mid]
                if nums[l]<=nums[mid]:
                    if target>=nums[l]:
                        r = mid-1
                    else:
                        l = mid+1
                else:
                    r = mid-1
            
        return -1
        