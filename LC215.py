import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = nums[:k]
        heapq.heapify(arr)
        for i in xrange(k, len(nums)):
            heapq.heappush(arr, nums[i])
            heapq.heappop(arr)
        
        return min(arr)