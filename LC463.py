class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def cal(x,y):
            t=0
            if x-1<0 or grid[x-1][y]==0:
                t+=1
            if x+1>=len(grid) or grid[x+1][y]==0:
                t+=1
            if y-1<0 or grid[x][y-1]==0:
                t+=1
            if y+1>=len(grid[0]) or grid[x][y+1]==0:
                t+=1
            return t
        ret = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]==1:
                    ret+=cal(i,j)
        return ret
            