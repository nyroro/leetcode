class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        l = 0
        r = n
        while l<r:
            mid = (l+r)/2
            t = mid*(mid+1)
            if t==2*n:
                return mid
            if t<2*n:
                l = mid
            else:
                r = mid
            if l == r-1:
                if r*(r+1)<2*n:
                    return r
                else:
                    return l
        return l
        