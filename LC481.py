from collections import Counter
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = "122"
        next_element = '1'
        next_index = 2
        while len(m)<n:
            m+=next_element * int(m[next_index])
            next_index+=1
            if next_element == '1':
                next_element = '2'
            else:
                next_element = '1'
                
        
        return Counter(m[:n])['1']
        