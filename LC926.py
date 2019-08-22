from collections import Counter
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def equal(word, ptn):
            table = {}
            rev_table = {}
            for i,t in enumerate(word):
                if t not in table and ptn[i] not in rev_table:
                    table[t] = ptn[i]
                    rev_table[ptn[i]] = t
                elif t in table and ptn[i] in rev_table:
                    if table[t] == ptn[i] and rev_table[ptn[i]] == t:
                        pass
                    else:
                        return False
                else:
                    return False
            return True
        
        ret = []
        for word in words:
            if equal(word,pattern):
                ret.append(word)
        return ret
        