from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        ret = ""
        for k,v in sorted(c.iteritems(), key = lambda x:(-x[1], x[0])):
            ret += k*v
        return ret
        
        