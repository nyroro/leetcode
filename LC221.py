class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        
        if len(matrix) == 0:
            return 0
        sums = [[0]*len(matrix[0]) for i in xrange(len(matrix))]
        
        ret = 0
        
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                sums[i][j] = int(matrix[i][j])
                if j>0:
                    sums[i][j]+=sums[i][j-1]
            if i>0:
                for j in xrange(len(matrix[i])):
                    sums[i][j]+=sums[i-1][j]
            
            for j in xrange(len(matrix[i])):
                if i==j and sums[i][j] == (i+1)*(i+1):
                    ret = max(ret, i+1)
                else:
                    for k in xrange(ret+1, min(i, j)+1):
                        if sums[i][j] - sums[i-k][j] - sums[i][j-k] + sums[i-k][j-k] == k*k:
                            ret = max(ret, k)
                    if i<j:
                        if sums[i][j] - sums[i][j-i-1] == (i+1)*(i+1):
                            ret = max(ret, i+1)
                    elif i>j:
                        if sums[i][j] - sums[i-j-1][j] == (j+1)*(j+1):
                            ret = max(ret, j+1)
        
        return ret*ret
                
                
                    
            