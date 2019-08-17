class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        t=x^y
        cnt = 0
        while t>0:
            cnt+=1
            t-=(t&-t)
        return cnt