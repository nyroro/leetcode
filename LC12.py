class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        def construct(one, five, ten, num):
            if num == 0:
                return ""
            if num <= 3:
                return one*num
            if num == 4:
                return one+five
            if num <= 8:
                return five + one*(num-5)
            if num==9:
                return one+ten
        a = construct('I','V','X', num%10)
        b = construct('X', 'L','C', (num//10)%10)
        c = construct('C','D','M',(num//100)%10)
        d = (num//1000)*'M'
        return d+c+b+a
            
        