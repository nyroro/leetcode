class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        index = len(digits)-1
        while index > 0 and digits[index]>=10:
            digits[index]%=10
            digits[index-1]+=1
            index -= 1
        if digits[0]>=10:
            digits[0]%=10
            digits.insert(0,1)
        return digits
        
        