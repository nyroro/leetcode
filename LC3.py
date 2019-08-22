class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        t = set()
        l = 0
        r = 1
        t.add(s[0])
        ret = 1
        while r<len(s):
            while l<r and s[r] in t:
                t.remove(s[l])
                l+=1
            t.add(s[r])
            r+=1
            ret = max(r-l,ret)
        return ret