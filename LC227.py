import re
digit = re.compile('\d+')
class Solution(object):
    def cal(self, op, a, b):
        if op == '+':return a+b
        elif op == '-':return a-b
        elif op == '*':return a*b
        else:return a//b
        
    def get_num(self, s):
        s = s.strip()
        num = digit.match(s).group(0)
        s = s[len(num):].strip()
        return int(num), s
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num, s = self.get_num(s)
        stack.append(num)
        
        while len(s)>0:
            stack.append(s[0])
            s = s[1:]
            next_num, s = self.get_num(s)
            if stack[-1] in '*/':
                op = stack.pop()
                stack[-1] = self.cal(op, stack[-1], next_num)
            else:
                stack.append(next_num)
        
        ret = stack[0]
        for i in xrange(1, len(stack), 2):
            ret = self.cal(stack[i], ret, stack[i+1])
        return ret
        
        
        
        