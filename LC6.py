class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ret = list(s)
        now = 0
        # 第一行
        for i in xrange(0, len(s), numRows-1+numRows-1):
            ret[now] = s[i]
            now+=1
        
        for i in xrange(1, numRows-1):
            start1 = i
            start2 = 2*numRows - i - 2
            next_d = numRows -1 + numRows-1
            now_d = 0
            
            # print i, start1, start2
            while start1 < len(s) or start2 < len(s):
                if now_d == 0:
                    ret[now] = s[start1]
                    start1+=next_d
                    now_d = 1
                    now+=1
                else:
                    ret[now] = s[start2]
                    start2+=next_d
                    now_d = 0
                    now+=1
        for i in xrange(numRows-1, len(s), numRows-1+numRows-1):
            ret[now] = s[i]
            now+=1
        return ''.join(ret)
        