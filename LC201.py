class Solution(object):
    def get_bits(self, m):
        ret = []
        while m>0:
            ret.append(m&1)
            m >>= 1
        return ret
        
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arrm = self.get_bits(m)
        arrn = self.get_bits(n)
        
        if(len(arrm) != len(arrn)):
            return 0
        
        index = max(len(arrm), len(arrn))
        result = []
        
        flag = True
        
        for t in xrange(index-1, -1, -1):
            if arrm[t] == arrn[t] and flag:
                result.append(arrm[t])
            else:
                flag = False
                result.append(0)
        ret = 0
        for v in result:
            ret = ret*2+v
        return ret