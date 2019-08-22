class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        table = {}
        for i,s in enumerate(S):
            table.setdefault(s,[]).append(i)
        ret = 0
        for value in table.itervalues():
            value = [-1]+value +[len(S)]
            for i in xrange(1,len(value)-1):
                ret+=(value[i]-value[i-1])*(value[i+1]-value[i])
        return ret%(10**9+7)
        