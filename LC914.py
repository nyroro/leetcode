import random
import bisect
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.t = [None]*len(rects)
        self.rects = rects
        for i, r in enumerate(self.rects):
            self.t[i] = (r[2]-r[0]+1)*(r[3]-r[1]+1)
        
        self.sums = sum(self.t)
        for i in xrange(1, len(self.t)):
            self.t[i] += self.t[i-1]

    def pick(self):
        """
        :rtype: List[int]
        """
        t1 = random.randint(0, self.sums-1)
        index = bisect.bisect(self.t, t1)
        r = self.rects[index]
        x1 = random.randint(r[0], r[2])
        x2 = random.randint(r[1], r[3])
        return [x1,x2]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()