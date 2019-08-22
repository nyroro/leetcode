from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        for i,t  in enumerate(s):
            if c[t]==1:
                return i
        return -1