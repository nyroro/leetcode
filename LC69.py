class Solution(object):
    def judge(self, t, x):
        if t*t == x:
            return True
        if t*t<x and (t+1)*(t+1)>x:
            return True
        return False
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0:return 0
        if x == 1:return 1
        l = 0
        r = x//2
        
        while l<r:
            mid = (l+r)/2
            if self.judge(mid, x):
                return mid
            if mid*mid > x:
                r = mid
            else:
                l = mid
            print l,r
            if l+1 == r:
                if self.judge(l, x):
                    return l
                else:
                    return r
        return l
        