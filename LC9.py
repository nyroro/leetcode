class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x<10:
            return True
        t = 0
        n = x
        while n>0:
            t=t*10+n%10
            n/=10
        return t==x
        