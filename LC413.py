class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3:
            return 0
        now = 2
        d = A[1]-A[0]
        ret = 0
        for i in xrange(2, len(A)):
            if A[i]-A[i-1] == d:
                now+=1
            else:
                ret += (now-2)*(now-1)/2
                now = 2
                d = A[i]-A[i-1]
        ret += (now-2)*(now-1)/2
        return ret