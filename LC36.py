class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            row = set()
            for j in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
        
        for i in xrange(9):
            col = set()
            for j in xrange(9):
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                    
        
        for i in xrange(9):
            block = set()
            for j in xrange(9):
                x = (i//3) * 3 + j//3
                y = (i%3) * 3 + j%3
                if board[x][y] != '.':
                    if board[x][y] in block:
                        return False
                    block.add(board[x][y])
        return True
                
        