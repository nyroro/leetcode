class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        l = max(A, E)
        b = max(B, F)
        
        r = min(C, G)
        u = min(D, H)
        print l,b,r,u
        
        area = (r-l)*(u-b)
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        
        print area1, area2, area
        
        if r-l < 0 or u-b<0:
            area = 0
        return area1 + area2 - area