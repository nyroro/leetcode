class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        nowHeight = 0
        ret = 0
        for i, t in enumerate(height):
            if len(stack) == 0:
                stack.append((i,t))
            elif t< stack[-1][1]:
                stack.append((i,t))
            else:
                
                nowHeight = 0
                while len(stack)>0 and t>=stack[-1][1]:
                    ret += (min(t, stack[-1][1])-nowHeight)*(i-stack[-1][0]-1)
                    nowHeight = min(t, stack[-1][1])
                    stack.pop(-1)
                if len(stack)>0:
                    ret += (min(t, stack[-1][1])-nowHeight)*(i-stack[-1][0]-1)
                    
                stack.append((i,t))
            print i,t,ret, nowHeight
        return ret
            
        