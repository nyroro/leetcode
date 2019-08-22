import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        lines = []
        for t in buildings:
            lines.append((t[0], "in", t[2]))
            lines.append((t[1], "out", t[2]))
        
        inq = []
        outq = []
        lines = sorted(lines)
        pre_top = 0
        ret = []
        for line in lines:
            if line[1] == "in":
                heapq.heappush(inq, -line[2])
            elif line[1] == 'out':
                heapq.heappush(outq, -line[2])
                while len(inq)>0 and len(outq)>0 and inq[0] == outq[0]:
                    heapq.heappop(inq)
                    heapq.heappop(outq)
            if len(inq)>0:
                now_top = -inq[0]
            else:
                now_top = 0
            if pre_top!=now_top:
                if len(ret)>0 and line[0]==ret[-1][0]:
                    ret[-1][1] = max(ret[-1][1], now_top)
                else:
                        
                    ret.append([line[0],now_top])
                pre_top = now_top
        return ret