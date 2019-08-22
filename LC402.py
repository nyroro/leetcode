class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):return "0"
        stack = []
        cnt = 0
        removes = set()
        for i in xrange(len(num)):
            if len(stack) == 0:
                stack.append(i)
            elif num[i]>=num[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and num[stack[-1]]>num[i] and k>0:
                    removes.add(stack[-1])
                    stack.pop(-1)
                    k-=1
                stack.append(i)
            if k<=0:
                break
        
        ret = []
        if k > 0:
            num = num[:len(num)-k]
        
        for i, t in enumerate(num):
            if i not in removes:
                ret.append(t)
        ret = ''.join(ret)
        ret = ret.lstrip('0')
        if ret == '':
            ret = '0'
        return ret
        