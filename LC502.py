import heapq
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        arr = []
        ret = W
        data = []
        for i in xrange(len(Capital)):
            data.append((Capital[i], Profits[i]))
        data = sorted(data)
        now = 0
        while now<len(data) and data[now][0]<=W:
            heapq.heappush(arr, -data[now][1])
            now+=1
        
        got = 0
        while got<k and len(arr)>0:
            ret += -arr[0]
            W+=-arr[0]
            got+=1
            heapq.heappop(arr)
            while now<len(data) and data[now][0]<=W:
                heapq.heappush(arr, -data[now][1])
                now+=1
        return ret
        