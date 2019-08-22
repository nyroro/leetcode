class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if len(matrix)==0:
            return ret
        now = [0,0]
        d = -1
        while len(ret) < len(matrix)*len(matrix[0]):
            print now
            if now[0] <0:
                d = -d
                now[0] +=1
            elif now[1]  < 0:
                d = -d
                now[1] += 1
            elif now[0]>=len(matrix):
                d = -d
                now[1] += 1
            elif now[1]>=len(matrix[0]):
                d = -d
                now[0]+=1
            while not (0<=now[0]<len(matrix) and 0<= now[1]<len(matrix[0])):
                print 'a',now
                now = [now[0]+d, now[1]-d]
            
                
            ret.append(matrix[now[0]][now[1]])
            now = [now[0]+d, now[1]-d]
        return ret
            