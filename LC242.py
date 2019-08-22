class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = {}
        
        for c in s:
            if c in ss:
                ss[c]+=1
            else:
                ss[c]=1
        for c in t:
            if c not in ss:
                return False
            ss[c] -= 1
        print ss.values()
        return all([t==0 for t in ss.values()])