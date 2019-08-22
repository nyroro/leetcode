from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pc = Counter(p)
        ret = []
        now = Counter(s[:len(p)])
        if now == pc:
            ret.append(0)
        for i in xrange(len(p),len(s)):
            now[s[i-len(p)]] -= 1
            if now[s[i-len(p)]]==0:
                now.pop(s[i-len(p)])
            now[s[i]]+=1
            # print now, pc
            if now == pc:
                ret.append(i-len(p)+1)
            
        return ret