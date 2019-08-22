class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0, 1]:
            return 0
        
        k = [1] * n
        k[0] = 0
        k[1] = 0
        
        for i in xrange(2, n):
            if i*i > n:
                break
            for j in xrange(i*i, n, i):
                k[j] = 0
        return sum(k)