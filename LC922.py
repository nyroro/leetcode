class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        table = {}
        for a,b in dislikes:
            table.setdefault(a,[]).append(b)
            table.setdefault(b,[]).append(a)
        color = [-1]*(N+1)
        
        def dfs(i, c):
            if color[i]==-1:
                color[i] = c
            else:
                if color[i]!=c:
                    return False
                else:
                    return True
            for k in table.get(i,[]):
                if not dfs(k, 1-c):
                    return False
            return True
        for i in xrange(1, N+1):
            if color[i]==-1 and not dfs(i, 0):
                return False
        return True
        