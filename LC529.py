class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
            
        d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        def mine_num(x, y):
            cnt = 0
            for di in d:
                dx = x+di[0]
                dy = y+di[1]
                if dx<0 or dx >= len(board):
                    continue
                if dy<0 or dy >= len(board[0]):
                    continue
                if board[dx][dy] == 'M':
                    cnt+=1
            return cnt
        l = [click]
        li = 0
        vis = [[False]*len(board[0]) for i in range(len(board))]
        vis[click[0]][click[1]]=True
        while li < len(l):
            x, y = l[li]
            li += 1
            e = []
            cnt = 0
            for di in d:
                dx = x+di[0]
                dy = y+di[1]
                if dx<0 or dx >= len(board):
                    continue
                if dy<0 or dy >= len(board[0]):
                    continue
                if board[dx][dy] == 'E':
                    if not vis[dx][dy]:
                        e.append([dx, dy])
                if board[dx][dy] == 'M':
                    cnt += 1
            if cnt > 0:
                board[x][y] = str(cnt)
            else:
                board[x][y] = 'B'
                for t in e:
                    l.append(t)
                    vis[t[0]][t[1]]=True
        return board
        