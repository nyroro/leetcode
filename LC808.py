import re
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        for word in words:
            index = 0
            t = 0
            while index < len(word):
                t = S.find(word[index], t)+1
                if t>0:
                    index+=1
                else:
                    break
            else:
                cnt+=1
            
        return cnt