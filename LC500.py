class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        A1 = set("QWERTYUIOP")
        A2 = set("ASDFGHJKL")
        A3 = set("ZXCVBNM")
        
        ret = []
        for word in words:
            if set(word.upper())|A1 == A1 or set(word.upper())|A2 == A2 or set(word.upper())|A3 == A3:
                ret.append(word)
        return ret