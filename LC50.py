class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n==0:
            return 1
        
        if n<0:
            return 1.0/self.myPow(x, -n)
        t = 1
        if n%2==1:
            t = x
        return t*self.myPow(x*x, n/2)
        