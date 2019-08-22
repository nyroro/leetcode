class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:return "0"
        sign = num>=0
        
        num = abs(num)
        ret = []
        while num>0:
            ret.append(str(num%7))
            num/=7
        if not sign:
            ret.append('-')
        return ''.join(ret[::-1])
        