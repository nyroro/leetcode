class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        now = 1
        ret = 0
        for i in xrange(len(s)-1, -1, -1):
            t = ord(s[i])-ord('A')+1
            ret += t*now
            now = now*26
        return ret