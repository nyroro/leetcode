from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()
        A = Counter(A)
        B = Counter(B)
        ret = []
        for key,value in A.iteritems():
            if value == 1:
                if key not in B:
                    ret.append(key)
                    
        for key,value in B.iteritems():
            if value == 1:
                if key not in A:
                    ret.append(key)
        return ret
            