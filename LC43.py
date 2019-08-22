class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # print num1, num2
        if len(num1) < len(num2) or (len(num1) == len(num2) and num1<num2):
            num1, num2 = num2, num1 
        if num2 == '0':return '0'
        if num2 == '1':return num1
        
        def plus(num1, num2):
            if len(num1)<len(num2):
                num1, num2 = num2, num1
            add = 0
            ret = []
            for i in xrange(len(num1)):
                index = -i-1
                if i<len(num2):
                    ret.append(ord(num1[index])-ord('0')+ord(num2[index])+add)
                else:
                    ret.append(ord(num1[index])+add)
                if ret[i] > ord('9'):
                    ret[i] = ret[i] - 10
                    add = 1
                else:
                    add = 0
                ret[i] = chr(ret[i])
            if add >0:
                ret.append('1')
            return ''.join(ret[::-1])
        def div(num1):
            ret = []
            mod = 0
            for t in num1:
                ret.append(chr((ord(t)-ord('0')+mod*10)/2 + ord('0')))
                mod = (ord(t)-ord('0'))%2
                
            if len(ret)>1 and ret[0] == '0':
                ret = ret[1:]
            return ''.join(ret)
        t1 = plus(num1, num1)
        t2 = div(num2)
        # print "r",t1,t2
        if (ord(num2[-1])-ord('0'))%2==0:
            return self.multiply(t1,t2)
        else:
            return plus(num1, self.multiply(t1,t2))
        