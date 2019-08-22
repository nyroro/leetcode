class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag1 = dividend < 0
        flag2 = divisor < 0
        flag = flag1 ^ flag2
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        arr = []
        tmp = divisor
        while tmp <= dividend:
            arr.append(tmp)
            tmp += tmp
        # print arr
        t_arr = []
        for i in xrange(len(arr)-1,-1,-1):
            if dividend >= arr[i]:
                t_arr.append(1)
                dividend -= arr[i]
            else:
                t_arr.append(0)
        # print 'result',t_arr
        ret = 0
        now = 1
        for i in xrange(len(t_arr)-1,-1,-1):
            if t_arr[i] == 1:
                ret += now
            now += now
        if flag:
            ret = -ret
        ret = min(0x7fffffff,ret)
        ret = max(-0x80000000, ret)
        return ret
                
            
        