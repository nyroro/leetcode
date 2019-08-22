import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        t = int(math.sqrt(area))
        for i in xrange(t+1, 0, -1):
            if area%i==0:
                t1 = max(area/i,i)
                t2 = min(area/i,i)
                return [t1,t2]