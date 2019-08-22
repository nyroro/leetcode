class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        while len(num1)<len(num2):
            num1 = "0"+num1
        while len(num2)<len(num1):
            num2 = "0"+num2
        
        res = 0
        ret = []
        for i in xrange(len(num1)-1,-1,-1):
            tmp = ord(num1[i])+ord(num2[i]) - 2*ord('0')+res
            if tmp > 9:
                tmp -= 10
                res = 1
            else:
                res = 0
            tmp = ord('0')+tmp
            ret.append(tmp)
        if res > 0:
            ret.append(ord('1'))
        ret = ret[::-1]
        ret = [chr(t) for t in ret]
        ret = ''.join(ret)
        return ret