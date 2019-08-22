class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.table = {}
        for t, val in zip(equations, values):
            
            self.table.setdefault(t[0], []).append((t[1], 1.0/val))
            self.table.setdefault(t[1], []).append((t[0], val))
        self.vals = {}
        for start in self.table.iterkeys():
            if start not in self.vals:
                self.vals[start] = (1.0, start)
                self.dfs(start, 1.0)
        ret = []
        for q in queries:
            if q[0] not in self.vals or q[1] not in self.vals:
                ret.append(-1)
            elif self.vals[q[0]][1] != self.vals[q[1]][1]:
                ret.append(-1)
            else:
                ret.append(self.vals[q[0]][0]/self.vals[q[1]][0])
        return ret
                
        
    def dfs(self, now, val):
        base = self.vals[now][1]
        for a, t in self.table[now]:
            if a not in self.vals:
                self.vals[a] = (val*t, base)
                self.dfs(a, val*t)
                