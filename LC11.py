class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<2:
            return 0
        l = 0
        r = len(height)-1
        ret = 0
        while l<r:
            dis = r-l
            val = min(height[l], height[r])
            ret = max(ret, dis*val)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return ret
            
        
        