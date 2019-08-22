class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0:
            return []
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(que):
            qi = 0
            ret = set(que)
            while qi<len(que):
                now = que[qi]
                qi+=1
                
                for dd in d:
                    nex = (now[0]+dd[0], now[1]+dd[1])
                    if 0<=nex[0]<len(matrix) and 0<=nex[1]<len(matrix[0]):
                        if matrix[nex[0]][nex[1]]>=matrix[now[0]][now[1]]:
                            if nex not in ret:
                                que.append(nex)
                                ret.add(nex)
            return ret
        a = []
        for i in xrange(0, len(matrix)):
            a.append((i,0))
        for j in xrange(1, len(matrix[0])):
            a.append((0,j))
        reta = bfs(a)
        b = []
        for i in xrange(0, len(matrix)):
            b.append((i,len(matrix[0])-1))
        for j in xrange(0, len(matrix[0])):
            b.append((len(matrix)-1,j))
        retb = bfs(b)
        return list(reta&retb)
                
                
        