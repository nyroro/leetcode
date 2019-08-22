class Solution(object):
    def dfs(self, x, y, mark):
        if x<0 or x>=self.width:
            return
        if y<0 or y>=self.height:
            return
        if self.grid[x][y]==0:
            return
        if self.island[x][y]!=0:
            return
        self.island[x][y] = mark
        self.cnt[mark] +=1
        self.dfs(x+1,y,mark)
        self.dfs(x-1,y,mark)
        self.dfs(x,y+1,mark)
        self.dfs(x,y-1,mark)
        
    def get_island(self, x, y):
        if x<0 or x>=self.width:
            return 0
        if y<0 or y>=self.height:
            return 0
        return self.island[x][y]
        
        
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.island = [[0]*len(grid[0]) for i in xrange(len(grid))]
        self.grid = grid
        self.cnt = {}
        mark = 1
        self.height = len(grid)
        self.width = len(grid[0])
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1 and self.island[i][j] == 0:
                    
                    self.cnt[mark] = 0
                    self.dfs(i, j, mark)
                    mark+=1
        ret = 0
        for key,value in self.cnt.iteritems():
            ret = max(ret, value)
                    
        for i in xrange(len(grid)):
            for j in xrange(len(grid)):
                if grid[i][j] == 0:
                    s = set()
                    s.add(self.get_island(i-1,j))
                    s.add(self.get_island(i+1,j))
                    s.add(self.get_island(i,j+1))
                    s.add(self.get_island(i,j-1))
                    s = list(s)
                    t = 1
                    for k in s:
                        t += self.cnt.get(k,0)
                    ret = max(ret, t)
        return ret
                    
        