import copy
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        table = {0:[], 1:["()"]}
        dfs_table = {0:[], 1:["()"]}
        def construct(n):
            if n in table:
                return table[n]
            arr = dfs(n-1)
            ret = []
            for t in arr:
                ret.append("(%s)"%t)
            table[n] = ret
            return ret
        def dfs(n):
            if n in dfs_table:
                return dfs_table[n]
            arr = construct(n)
            ret = copy.copy(arr)
            for i in xrange(1,n):
                arr = construct(i)
                arr2 = dfs(n-i)
                for t1 in arr:
                    for t2 in arr2:
                        ret.append(t1+t2)
            dfs_table[n]=ret
            return ret
        return dfs(n)
            
            
            
            
        