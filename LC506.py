class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = [None] * len(nums)
        
        arr = zip(nums, range(len(nums)))
        arr = sorted(arr)[::-1]
        
        ret[arr[0][1]] = "Gold Medal"
        if len(arr)>1:
            ret[arr[1][1]] = "Silver Medal"
        if len(arr)>2:
            ret[arr[2][1]] = "Bronze Medal"
        
        for i in xrange(3, len(arr)):
            ret[arr[i][1]] = str(i+1)
        return ret
        