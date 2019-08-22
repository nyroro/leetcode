class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n<10:
            return k
        k-=1
        arr = [1]
        for i in xrange(1, len(str(n))):
            arr.append(arr[-1]+(10**i))
        ret = [0]
        def cal(n_str, k, si):
            # print 'cal', n_str, k, si
            if len(n_str)==1:
                ret[0] = ret[0]*10+k
                return
            for i in xrange(si, 10):
                if i < int(n_str[0]):
                    now = arr[len(n_str)-1]
                elif i==int(n_str[0]):
                    now = arr[len(n_str)-2] + int(n_str[1:]) + 1
                else:
                    now = arr[len(n_str)-2]
                if k>=now:
                    k-=now
                    # print i, now
                else:
                    result = i
                    break
            ret[0] = ret[0]*10 + result
            if k==0:
                return
            k-=1
            if result < int(n_str[0]):
                n_str = '9'*(len(n_str))
            elif result > int(n_str[0]):
                n_str = '9'*(len(n_str)-1)
            cal(n_str[1:], k, 0)
            
        cal(str(n), k, 1)
        return ret[0]
            