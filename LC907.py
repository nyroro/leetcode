class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        a = 1
        b = max(piles)
        
        while a<b:
            mid = (a+b)/2
            time = 0
            for pile in piles:
                time+=pile/mid
                if pile%mid!=0:
                    time+=1
            
            if time <= H:
                b = mid
            else:
                a = mid+1
        return b
        