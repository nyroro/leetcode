import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        m = int(math.log(n,2))
        for i in xrange(m,1,-1):
            k = int(math.pow(n, 1.0/i))
            print k
            if k<=1:continue
            t1 = (k**(i+1)-1)
            t2 = (k-1)
            if t1 == t2*n:
                return str(k)
        return str(n-1)
                
            