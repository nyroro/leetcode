class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        height = len(matrix)
        for i in xrange(height/2+height%2):
            for j in xrange(width/2):
                matrix[i][j], matrix[width-j-1][i], matrix[height-i-1][width-j-1],matrix[j][height-i-1] = matrix[width-j-1][i], matrix[height-i-1][width-j-1],matrix[j][height-i-1],matrix[i][j]