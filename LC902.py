import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        now = startFuel
        
        if now >= target:
            return 0
        arr = []
        ret = 0
        for t in stations:
            if t[0] > now:
                while len(arr)>0 and now < t[0]:
                    print arr[0]
                    now -= heapq.heappop(arr)
                    ret += 1
            
            if now >= target:
                return ret
            
            if t[0]<= now:
                heapq.heappush(arr,-t[1])
        while len(arr)>0 and now<target:
            print arr[0]
            now-=heapq.heappop(arr)
            ret+=1
            
        if now>=target:
            return ret
        else:
            return -1
            
            
        