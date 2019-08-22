class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        table = set()
        ret = set()
        for i in xrange(len(s)):
            if i>=9:
                t = s[i-10+1:i+1]
                if t in table:
                    ret.add(t)
                else:
                    table.add(t)
        return list(ret)
                