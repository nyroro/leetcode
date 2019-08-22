class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        t = 10
        cnt = 1
        while n>=t*cnt:
            n-=t*cnt
            t = 9*(10**cnt)
            cnt+=1
            
        num = n/cnt+10**(cnt-1)
        t = n%cnt
        return int(str(num)[t])