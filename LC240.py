class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >=0:
            if matrix[i][j] > target:
                j-=1
            elif matrix[i][j] == target:
                return True
            else:
                i+=1
            
        return False
        