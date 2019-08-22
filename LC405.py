class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        ret = []
        t = abs(num)
        if num<0:
            t-=1
        while t>0:
            ret.append(t%16)
            t/=16
        if num>0:
            for i in xrange(len(ret)):
                if ret[i]<10:
                    ret[i] = chr(ord('0')+ret[i])
                else:
                    ret[i] = chr(ord('a')+ret[i]-10)
            
        else:
            ret = ret + [0]*(8-len(ret))
            print ret
            for i in xrange(len(ret)):
                t = 15-ret[i]
                if t<10:
                    ret[i] = chr(ord('0')+t)
                else:
                    ret[i] = chr(ord('a')+t-10)
        return ''.join(ret[::-1])
        