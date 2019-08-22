class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        table1 = {}
        table2 = {}
        for i in xrange(len(s)):
            if s[i] not in table1 and t[i] not in table2:
                table1[s[i]] = t[i]
                table2[t[i]] = s[i]
            else:
                if table1.get(s[i])!=t[i] or table2.get(t[i])!=s[i]:
                    return False
        return True