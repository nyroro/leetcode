class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i,t in enumerate(nums):
            if t<=0 or t>len(nums):
                continue
            while nums[i]!=i+1 and 1<=nums[i]<=len(nums) and nums[nums[i]-1] != nums[i]:
                t = nums[i]
                index = nums[i]-1
                nums[i] = nums[nums[i]-1]
                nums[index] = t
        for i,t in enumerate(nums):
            if t!=i+1:
                return i+1
        return len(nums)+1
        
                