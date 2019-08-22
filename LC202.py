class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        used = set([n])
        
        while True:
            k = [int(t) for t in str(n)]
            n = sum([t*t for t in k])
            if n == 1:
                break
            if n in used:
                return False
            used.add(n)
        return True