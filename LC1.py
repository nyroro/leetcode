class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums)-1
        nums = sorted(zip(nums, range(len(nums))))
        
        
        while i<j:
            t = nums[i][0] + nums[j][0]
            if t == target:
                return nums[i][1], nums[j][1]
            
            if t < target:
                i += 1
            else:
                j -= 1