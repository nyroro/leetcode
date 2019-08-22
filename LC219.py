class Solution(object):
    
    def insert(self, num_set, k):
        if k in num_set:
            return False
        num_set.add(k)
        return True
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_set = set()
        
        for i in xrange(min(k+1, len(nums))):
            if not self.insert(num_set, nums[i]):
                return True
        
        for i in xrange(k+1, len(nums)):
            num_set.remove(nums[i-k-1])
            if not self.insert(num_set, nums[i]):
                return True
        return False
            
        