class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=26:
            return chr(ord('A')+n-1)
        else:
            n -= 26
            t = (n-1)%26+1
            t2 = (n-1)/26 + 1
            return self.convertToTitle(t2)+self.convertToTitle(t)