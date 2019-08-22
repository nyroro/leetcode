import re
class Solution(object):
    
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+':lambda x,y:x+y,
                  '-':lambda x,y:x-y,
                  '*':lambda x,y:x*y}.get, tokens[1::2])
        def dfs(l, r):
            if l == r:
                return [nums[l]]
            ret = []
            for mid in xrange(l, r):
                for a in dfs(l,mid):
                    for b in dfs(mid+1,r):
                        ret.append(ops[mid](a,b))
            return ret
            
        
                  
        return dfs(0, len(nums)-1)