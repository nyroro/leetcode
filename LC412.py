class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for t in xrange(1,n+1):
            if t%3==0 and t%5==0:
                ret.append('FizzBuzz')
            elif t%3==0:
                ret.append('Fizz')
            elif t%5==0:
                ret.append('Buzz')
            else:
                ret.append(str(t))
        return ret
        