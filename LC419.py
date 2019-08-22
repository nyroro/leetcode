class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                flag = board[i][j]=='X'
                if i>0 and board[i-1][j]=='X':
                    flag = False
                if j>0 and board[i][j-1]=='X':
                    flag = False
                if flag:
                    ret += 1
        return ret
        