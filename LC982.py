from collections import Counter
import heapq
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        c = Counter(A)
        arr = []
        ret = 0
        for key in c.iterkeys():
            heapq.heappush(arr, key)
        while len(arr) > 0:
            key = heapq.heappop(arr)
            print key, c[key]
            if c[key]-1 > 0 and key+1 not in c:
                heapq.heappush(arr,key+1)
            if c[key]-1>0:
                ret+=c[key]-1
                c[key+1] += c[key]-1
        return ret
        
        