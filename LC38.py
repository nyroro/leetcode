class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        say=self.countAndSay(n-1)
        now = say[0]
        cnt = 1
        ret = ''
        for i in xrange(1, len(say)):
            if now == say[i]:
                cnt+=1
            else:
                ret += str(cnt)+str(now)
                now = say[i]
                cnt = 1
        ret += str(cnt)+str(now)
        return ret