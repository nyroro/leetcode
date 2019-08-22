import re

digit = re.compile('\d+')
def cal(op, a, b):
    if op == '+':
        return a+b
    else:
        return a-b
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s.replace(' ','')+')'
        return self.cal_step(0)[0]
    
    
    
    def cal_step(self, index):
        num = 0
        op = '+'
        
        while self.s[index] != ')':
            if self.s[index] == '(':
                next_num, index = self.cal_step(index+1)
                num = cal(op, num, next_num)
            elif self.s[index] in ('+', '-'):
                op = self.s[index]
                index += 1
            else:
                result = digit.match(self.s[index:])
                result = result.group(0)
                next_num = int(result)
                num = cal(op, num, next_num)
                index += len(result)
        return num, index+1
            
        
            
        