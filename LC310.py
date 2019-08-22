import copy
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if n == 1:
            return [0]
        graph = {}
        degree = [0]*n
        for e in edges:
            graph.setdefault(e[0], set()).add(e[1])
            graph.setdefault(e[1], set()).add(e[0])
            
        que = []
        ans_set = set(range(n))
        
        for k, v in graph.iteritems():
            if len(v) == 1:
                que.append(k)
                
        while len(ans_set)>2:
            next_que = []
            
            for now in que:
                ans_set.remove(now)
                nodes = graph[now]
                nex = list(nodes)[0]
                graph[nex].remove(now)
                if len(graph[nex])==1:
                    next_que.append(nex)
            que = next_que
        return list(ans_set)
                
                
                