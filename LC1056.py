class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        def cal(W):
            ret = 0
            now = 0
            for t in weights:
                if now+t<=W:
                    now+=t
                else:
                    now = t
                    ret+=1
            return ret+1
        num = -1
        while l<r:
            if l == r-1:
                if cal(l)<=D:
                    num=l
                else:
                    num = r
                break
                    
            mid = (l+r)/2
            if cal(mid) > D:
                l = mid
            else:
                r = mid
                num = r
        return num
            
            
        
        