class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = range(1,n+1)
        def permute(n,k,arr):
            if n==1:
                return str(arr[0])
            div = reduce(lambda x,y:x*y, range(1,n))
            s = arr[k/div]
            arr.remove(s)
            return str(s)+permute(n-1,k%div,arr)
        return permute(n,k-1,arr)