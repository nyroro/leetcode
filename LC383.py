from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = Counter(ransomNote)
        b = Counter(magazine)
        
        for key,value in a.iteritems():
            if key in b and b[key]>=value:
                pass
            else:
                return False
        return True
        