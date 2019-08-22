class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip())==0:
            return 0
        return len(s.split()[-1])