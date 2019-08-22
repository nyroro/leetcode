class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        while num & 3 ==0:
            num>>=2
        return num==1
        