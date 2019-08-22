class Node(object):
    def __init__(self):
        self.next = {}
        self.end = False
        self.word = ''

class Solution(object):
    
    def insert(self, word):
        now = self.root
        for character in word:
            if character not in now.next:
                now.next[character] = Node()
            now = now.next[character]
        now.end = True
        now.word = word
        
    def build_tries(self, words):
        self.root = Node()
        for word in words:
            self.insert(word)
    
    def dfs(self, board, i, j, now_node):
        if board[i][j] in now_node.next:
            now_node = now_node.next[board[i][j]]
        else:
            return
        if now_node.end:
            self.ret.add(now_node.word)
        self.visits[i][j] = True
        
        steps = [[0,1],[0,-1],[1,0], [-1,0]]
        for step in steps:
            ni, nj = i+step[0], j+step[1]
            if 0<=ni<len(board) and 0<=nj<len(board[0]):
                if not self.visits[ni][nj]:
                    self.dfs(board, ni, nj, now_node)
        
        
        self.visits[i][j] = False
            
            
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.build_tries(words)
        
        if len(board) == 0 or len(board[0]) == 0:
            return []
        
        self.ret = set()
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.visits = [[False]*len(board[0]) for k in xrange(len(board))]
                self.dfs(board, i, j, self.root)
        return list(self.ret)
        