class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        t = A[0]
        l = 0
        r = len(A)-1
        while l<r:
            while l<r and A[r]%2==1:
                r-=1
            if l<r:
                A[l] = A[r]
            while l<r and A[l]%2==0:
                l+=1
            if l<r:
                A[r] = A[l]
        A[l] = t
        return A
        