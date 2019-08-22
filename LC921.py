import copy
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        now = [r0, c0]
        ret = []
        ret.append(copy.copy(now))
        d = [(0,1),(1, 0),(0,-1),(-1,0)]
        cnt = 0
        i = 0
        while len(ret) < R*C:
            num = cnt / 2 + 1
            for j in xrange(num):
                now[0] += d[i][0]
                now[1] += d[i][1]
                if 0<=now[0]<R and 0<=now[1]<C:
                    ret.append(copy.copy(now))
            cnt += 1
            i = (i+1)%len(d)
        return ret
        