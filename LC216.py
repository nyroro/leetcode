import copy
class Solution(object):
    
    def dfs(self, k, n, index, arr):
        if k==0 and n==0:
            self.ret.append(copy.copy(arr))
            return
        for i in xrange(index+1, 10):
            arr.append(i)
            self.dfs(k-1, n-i, i, arr)
            arr.pop()
        
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if(k*9<n):
            return []
        self.ret = []
        self.dfs(k, n, 0, [])
        
        return self.ret