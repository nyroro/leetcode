from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)==0:
            return 0
        cs = Counter(s)
        if min(cs.itervalues())>=k:
            return len(s)
        l=0
        ans = 0
        for i in xrange(len(s)):
            if cs[s[i]]<k:
                r = i
                if r-1>=l:
                    ret = self.longestSubstring(s[l:r],k)
                    ans=max(ans,ret)
                l=i+1
        if len(s)-1>=l:
            ret =self.longestSubstring(s[l:],k)
            ans=max(ans,ret)
        return ans
        