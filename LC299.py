from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = 0
        t = Counter(secret)
        b = 0
        vis = set()
        for i in xrange(len(secret)):
            if secret[i]==guess[i]:
                a+=1
                t[guess[i]]-=1
                vis.add(i)
        for i in xrange(len(secret)):
            if guess[i] in t and t[guess[i]]>0 and i not in vis:
                b+=1
                t[guess[i]]-=1
        return '%dA%dB'%(a,b)