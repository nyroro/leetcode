class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ['0']*n
        vis = {''.join(res)}
        def dfs():
            now = ''.join(res[-n+1:])
            if n == 1:
                now = ''
            
            # print res,vis
            for i in xrange(k-1,-1,-1):
                next = now + str(i)
                if next not in vis:
                    vis.add(next)
                    res.append(str(i))
                    dfs()
                    return
        dfs()
        return ''.join(res)
        
        
            
        