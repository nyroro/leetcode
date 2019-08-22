class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = int(1e9+7)
        A.sort()
        dp = [1]*len(A)
        table = {}
        ret = 0
        for i in xrange(len(A)):
            for j in xrange(i):
                if A[i]%A[j] == 0 and (A[i]//A[j]) in table:
                    dp[i]+=dp[j]*dp[table[A[i]//A[j]]]
                    dp[i]%=mod
            ret += dp[i]
            ret %= mod
            table[A[i]] = i
        return ret
        