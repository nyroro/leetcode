class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-','')
        ret = [S[:len(S)%K]]+[S[len(S)%K + K*i: len(S)%K + K*(i+1)]for i in xrange(len(S)//K)] 
        return '-'.join(ret).upper().lstrip('-')