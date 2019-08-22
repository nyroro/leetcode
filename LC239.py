import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        inq = []
        outq = []
        ret = []
        for i in xrange(len(nums)):
            if i >= k:
                heapq.heappush(outq, -nums[i-k])
                while(len(outq)>0 and inq[0] == outq[0]):
                    heapq.heappop(inq)
                    heapq.heappop(outq)
                
            
            heapq.heappush(inq, -nums[i])
            if i>=k-1:
                ret.append(-inq[0])
        print ret
        return ret
            