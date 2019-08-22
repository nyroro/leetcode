import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        t = re.match("\s*([+-]?\d+)", str)
        if t==None:
            return 0
        t = t.group(1)
        # print t.group(1)
        
        ret = 0
        sign = 1
        if t[0]=='+':
            pass
            t = t[1:]
        elif t[0]=='-':
            sign = -1
            t = t[1:]
        for c in t:
            ret = ret*10 + ord(c)-ord('0')
        ret = sign*ret
        if ret > 0x7fffffff:
            ret = 0x7fffffff
        if ret < -(2**31):
            ret = -(2**31)
        
        return ret
        