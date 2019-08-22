class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret = 0
        for i in xrange(ord('A'), ord('Z')+1):
            rep = 0
            cons = 0
            now = 0
            for j in xrange(len(s)):
                if s[j] == chr(i):
                    cons += 1
                else:
                    rep += 1
                while rep>k:
                    if s[now]==chr(i):
                        cons-=1
                    else:
                        rep-=1
                    now+=1
                ret = max(ret, cons+rep)
        return ret