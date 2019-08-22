import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t1 = r"(([\+\-]?\d+)|([\+\-]?\d*\.\d+)|([\+\-]?\d+\.\d*))"
        t2 = r"(%s$)|(%se([\+\-]?\d+)$)"%(t1,t1)
        return re.match(t2, s.strip()) != None
        