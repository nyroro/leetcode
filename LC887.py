import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        arr = []
        for q,w in zip(quality, wage):
            arr.append((1.0*w/q, q))
            
        arr = sorted(arr)
        heap = []
        sums = 0
        for i in xrange(K):
            sums += arr[i][1]
            heap.append(-arr[i][1])
        heapq.heapify(heap)
        ret = 1.0*sums*arr[K-1][0]
        
        for i in xrange(K,len(quality)):
            
            sums += arr[i][1]
            heapq.heappush(heap, -arr[i][1])
            
            sums += heapq.heappop(heap)
            ret = min(ret,1.0*sums*arr[i][0])
        return ret
        
        