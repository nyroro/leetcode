import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        t = set()
        for i in xrange(len(nums)):
            if nums[i] not in t:
                heapq.heappush(arr,nums[i])
                t.add(nums[i])
                if len(arr)>3:
                    tmp = heapq.heappop(arr)
                    t.remove(tmp)
        
        if len(arr)!=3:
            while len(arr)>1:
                heapq.heappop(arr)
        return arr[0]
        