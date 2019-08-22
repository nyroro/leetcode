import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        table = {}
        for u,v,cost in flights:
            table.setdefault(u,[]).append((v,cost))
        que = []
        # cost, time, node
        heapq.heappush(que, (0, 0, src))
        
        ret = -1
        
        while len(que)>0:
            cost,time,node = heapq.heappop(que)
            # print 'ddd',cost,time,node
            if time > K:
                continue
            if ret!=-1 and cost>=ret:
                continue
            # print cost,time,node
            for v,v_cost in table.get(node, []):
                if v==dst:
                    if ret==-1:
                        ret = cost+v_cost
                    else:
                        ret = min(ret,v_cost+cost)
                else:
                    # print '?!?!?!'
                    heapq.heappush(que,(cost+v_cost, time+1, v))
        return ret
            
            
            