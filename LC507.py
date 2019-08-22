
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:return False
        i = 2
        ret = 1
        while i*i<=num and ret<=num:
            if num%i==0:
                ret+=num/i+i
            i+=1
        return ret == num
        