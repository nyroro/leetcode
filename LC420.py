class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [0, 0, 0]
        for t in s:
            if t.islower():
                letters[0] = 1
            if t.isupper():
                letters[1] = 1
            if t.isdigit():
                letters[2] = 1
        ret1 = 3 - sum(letters)
        now = ''
        cnt = 0
        ret2 = 0
        table = {}
        for i in xrange(len(s)):
            if s[i]==now:
                cnt+=1
            else:
                if cnt>=3:
                    table[cnt]=table.get(cnt,0)+1
                now = s[i]
                cnt = 1
        if cnt>=3:
            table[cnt]=table.get(cnt,0)+1
        if len(s)<6:
            ret3= 6-len(s)
            ret2 = sum([(k/3)*v for k, v in table.iteritems()])
            return max([ret1, ret2, ret3])
        elif len(s)>20:
            ret3 = len(s)-20
            t = ret3
            for k in table.keys():
                if k%3==0:
                    num = min(table[k], t)
                    table[k]-=num
                    if k-1>3:
                        table[k-1] = table.get(k-1,0)+num
                    t-=num
            for k in table.keys():
                if k%3 == 1:
                    num = min(table[k], t/2)
                    table[k] -= num
                    if k-2>3:
                        table[k-2] = table.get(k-2,0)+num
                    t-=num*2
                
            ret2 = sum([(k/3)*v for k, v in table.iteritems() if k%3!=2])
            
            ret2_ = sum([(k/3)*v for k, v in table.iteritems() if k%3==2]) - t/3
            print ret1, ret2, ret3
            return ret3+max(ret2+ret2_,ret1)
        else:
            
            ret2 = sum([(k/3)*v for k, v in table.iteritems()])
            return max(ret2, ret1)