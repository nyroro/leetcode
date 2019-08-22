import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(nums, i):
            if i == len(nums):
                ret.append(copy.copy(nums))
                return
            for j in xrange(i, len(nums)):
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
                dfs(nums, i+1)
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
        dfs(nums, 0)
        return ret
                
        