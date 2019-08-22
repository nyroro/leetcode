class Solution(object):
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ret = 0
        def cal(mid, r, one, s):
            ret = 0
            cnt = 0
            for i, t in enumerate(s):
                if t not in [mid,r,one]:
                    s = s[i:]
                    break
                if t==r:
                    ret += 10 - cnt
                    cnt = 0
                elif t == mid:
                    ret += 5 - cnt
                    cnt = 0
                else:
                    cnt += 1
            else:
                s = ''
            ret += cnt
            return ret,s
        tmp, s = cal('D','M','C',s)
        ret += tmp*100
        # print ret,s
        tmp, s = cal('L','C','X',s)
        ret+=tmp*10
        # print ret,s
        tmp, s = cal('V','X','I',s)
        ret+=tmp
        # print ret,s
        
        return ret
                    
                
        