class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        r = 0
        i = 0
        ret = 0
        while r<n:
            if i<len(nums) and r>=nums[i]-1:
                r+=nums[i]
                i+=1
            else:
                r+=(r+1)
                ret+=1
        return ret
                