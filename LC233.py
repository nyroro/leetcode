arr = [0,1]
def construct_arr(n):
    for i in xrange(len(arr), n):
        arr.append(10*arr[-1]+10**(i-1))
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        m = len(str(n))
        construct_arr(m+1)
        if m == 1:
            if n==0:return 0
            else:return 1
        k = n//(10**(m-1))
        b = n%(10**(m-1))
        if k==1:
            ret = arr[m-1]+b +1+self.countDigitOne(b)
        else:
            ret = arr[m-1]*(k)+10**(m-1)+self.countDigitOne(b)
        return ret
        
        