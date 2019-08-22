class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        arr = range(0,10)
        if N == 1:
            return arr
        arr = range(1,10)
        for i in xrange(1,N):
            next_arr = []
            for t in arr:
                digit = t%10
                if digit+K<10:
                    next_arr.append(t*10+digit+K)
                if K!=0 and digit-K>=0:
                    next_arr.append(t*10+digit-K)
            arr = next_arr
        return arr