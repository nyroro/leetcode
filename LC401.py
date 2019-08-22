class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def cal(num, m):
            ret = []
            for i in xrange(m):
                cnt = 0
                t = i
                while t>0:
                    cnt += t%2
                    t/=2
                if cnt == num:
                    ret.append(i)
            return ret
        ret = []
        for i in xrange(num+1):
            a = cal(i, 12)
            b = cal(num-i, 60)
            
            for j in a:
                for k in b:
                    # print j,k
                    ret.append('%d:%02d'%(j,k))
        return ret