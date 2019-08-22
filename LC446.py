class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tables = [None]*len(A)
        if len(A)==0:
            return 0
        tables[0] = {}
        ret = 0
        for i in xrange(1, len(A)):
            tables[i] = {}
            for j in xrange(0,i):
                t = A[i]-A[j]
                if t not in tables[i]:
                    tables[i][t] = 0
                tables[i][t] += tables[j].get(t, 0)+1
                if tables[j].get(t,0)>=1:
                    ret += tables[j].get(t,0)
        return ret
        
        