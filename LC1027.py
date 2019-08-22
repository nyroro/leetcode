class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sumA = sum([t for t in A if t%2==0])
        ret = []
        for q in queries:
            pre = A[q[1]]
            if pre%2==0:
                sumA-=pre
            A[q[1]]+=q[0]
            if A[q[1]]%2==0:
                sumA+=A[q[1]]
                
            ret.append(sumA)
        return ret