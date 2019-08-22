class Solution(object):
    def tarjan(self, x, pre):
        self.cnt+=1
        self.dfn[x]=self.cnt
        self.low[x]=self.cnt
        num = 0
        mal = 0
        safe_num = 0
        cut = False
        son = 0
        for i in xrange(len(self.graph)):
            if i in [x, pre]:
                continue
            if not self.graph[x][i]:
                continue
            if self.dfn[i]:
                self.low[x] = min(self.low[x], self.dfn[i])
            else:
                ret = self.tarjan(i, x)
                son += 1
                num += ret[0]
                mal += ret[1]
                if ret[1] == 0:
                    safe_num+=ret[0]
                self.low[x] = min(self.low[x], self.low[i])
                if pre != -1 and self.low[i]>=self.dfn[x]:
                    cut=True
                elif pre == -1 and son>1:
                    cut = True
        num += 1
        mal += (1 if x in self.initial else 0)
        if x in self.initial:
            if cut:
                up_mal = self.block_mal[self.block[x]] - mal
                if up_mal == 0:
                    safe_num += self.block_num[self.block[x]]-num
                
                if safe_num > self.safe_num:
                    self.safe_num = safe_num
                    self.ret = x
                elif safe_num == self.safe_num:
                    self.ret = min(self.ret, x)
            elif self.block_mal[self.block[x]] == 1 and self.block_num[self.block[x]]>1:
                safe_num = self.block_num[self.block[x]] - 1
            
                if safe_num > self.safe_num:
                    self.safe_num = safe_num
                    self.ret = x
                elif safe_num == self.safe_num:
                    self.ret = min(self.ret, x)
                
        return num, mal
    
    def dfs(self, now, pre):
        self.block[now]=self.block_cnt
        num = 1
        mal = 1 if now in self.initial else 0
        for i in xrange(len(self.graph)):
            if i in [now,pre]:
                continue
            if not self.graph[now][i]:
                continue
            if self.block[i]>=0:
                continue
            a, b = self.dfs(i,now)
            num+=a
            mal+=b
        return num, mal
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        self.graph = graph
        self.initial = set(initial)
        self.block = [-1]*len(graph)
        self.block_num = []
        self.block_mal = []
        self.block_cnt = 0
        self.ret = len(graph)
        self.safe_num = 0
        for i in xrange(len(graph)):
            if self.block[i]<0:
                num, mal = self.dfs(i, -1)
                self.block_num.append(num)
                self.block_mal.append(mal)
                self.block_cnt+=1
        self.dfn = [0]*len(graph)
        self.low = [0]*len(graph)
        self.cnt = 0
        for i in xrange(len(graph)):
            if not self.dfn[i]:
                self.tarjan(i, -1)
        if self.ret == len(graph):
            self.ret = min(initial)
        return self.ret