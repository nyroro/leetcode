class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        arr = []
        ret  =0
        for i in xrange(1,len(A)):
            arr.append({})
            for j in xrange(i):
                t = A[i] - A[j]
                if t in arr[j-1]:
                    arr[i-1][t] = max(arr[i-1].get(t,0), arr[j-1][t]+1)
                else:
                    arr[i-1][t] = max(arr[i-1].get(t,0), 2)
                ret  =max(ret, arr[i-1][t])
        return ret
                
                
        