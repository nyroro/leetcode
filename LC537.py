import re
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r1 = re.match('([\d-]+)\+([\d-]+)i', a)
        r2 = re.match('([\d-]+)\+([\d-]+)i', b)
        a1 = int(r1.group(1))
        a2 = int(r1.group(2))
        b1 = int(r2.group(1))
        b2 = int(r2.group(2))
        
        t1 = a1*b1-a2*b2
        t2 = a1*b2+a2*b1
        
        return '%d+%di'%(t1,t2)