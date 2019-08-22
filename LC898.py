class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [[A[j][i] for j in xrange(len(A))] for i in xrange(len(A[0]))]
        return B
        