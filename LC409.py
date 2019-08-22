from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        two=0
        one = 0
        for key, value in c.iteritems():
            if value%2==0:
                two+=value
            else:
                two+=(value//2)*2
                one = 1
        return two+one
        