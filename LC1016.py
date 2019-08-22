from collections import Counter
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sums = [0]
        for t in A:
            sums.append((sums[-1]+t)%K)
        ret = 0
        sums = Counter(sums)
        for value in sums.itervalues():
            if value>1:
                ret+=value*(value-1)/2
        return ret
        
                
            
        
        