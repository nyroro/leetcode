class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a = m
        b = n
        for t in ops:
            a = min(t[0], a)
            b = min(t[1], b)
        return a*b