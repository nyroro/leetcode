class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        now = None
        flag = False
        for t in nums:
            if now is None:
                now = t
                ret.append(str(now))
            elif now != t-1:
                if flag:
                    ret[-1] += "->"+str(now)
                flag = False
                now = t
                ret.append(str(now))
                
            else:
                flag = True
                now = t
        if flag:
            ret[-1]+="->"+str(now)
        return ret
                
                
        
        