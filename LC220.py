import heapq
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k==0:
            return False
        table = {}
        
        for i in xrange(len(nums)):
            key = nums[i]//max(1, t)
            for m in (key-1,key,key+1):
                if m in table:
                    if abs(table[m] - nums[i])<=t:
                        return True
            
            if i>=k:
                t_key = nums[i-k]//max(1,t)
                table.pop(t_key, None)
            table[key] = nums[i]
            
        return False
            