class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        t1 = A[i]
        t2 = A[j]
        
        def cal(arr):
            if len(arr)==0:return -1
            ret = 0
            for t in arr:
                ret = ret*2+t
            return ret
        t3 = cal(A[j+1:])
        while j<len(A):
            if t1 == t2:
                if t3 == t2:
                    return [i,j+1]
                
            if t2<=t1:
                j+=1
                if j<len(A):
                    t2 = t2*2+A[j]
                    t3 -= (A[j]<<(len(A)-j-1))
            while i<j and t1<t2:
                t2 -= (A[i+1]<<(j-i-1))
                i += 1
                t1 = t1*2+A[i]
        return -1,-1
        