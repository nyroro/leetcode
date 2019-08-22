class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k==1:
            return s
        ret = ''
        for i in xrange(0, len(s), 2*k):
            if i+2*k<len(s):
                ret+=s[i:i+k][::-1]+s[i+k:i+2*k]
            elif i+k>=len(s):
                ret+=s[i:][::-1]
            else:
                ret += s[i:i+k][::-1] + s[i+k:]
                
                
        return ret
        