import copy
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums = sorted(nums)
        def permute(nums, index):
            if index == len(nums):
                ret.append(copy.copy(nums))
                return
            nums[index:] = sorted(nums[index:])
            permute(nums, index + 1)
            for i in xrange(index+1, len(nums)):
                if nums[i]!=nums[i-1]:
                    print 'start', nums, index, i
                    nums[i],nums[index]  =nums[index], nums[i]
                    permute(copy.copy(nums), index + 1)
                    nums[i],nums[index]  =nums[index], nums[i]
                    
                    print 'end', nums, index, i
                    
        permute(nums, 0)
        return ret
            