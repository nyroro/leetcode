class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        inserted = False
        tmp = newInterval
        for t in intervals:
            if t[1]<newInterval[0]:
                ret.append(t)
            elif t[0]>newInterval[1]:
                if not inserted:
                    ret.append(tmp)
                    inserted = True
                ret.append(t)
            else:
                tmp[0] = min(tmp[0],t[0])
                tmp[1] = max(tmp[1],t[1])
        if not inserted:
            ret.append(tmp)
        return ret
                    
                            
        