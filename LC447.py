class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in xrange(len(points)):
            table = {}
            for j in xrange(len(points)):
                if i==j:continue
                t1 = points[i]
                t2 = points[j]
                dis = (t1[0]-t2[0])**2+(t1[1]-t2[1])**2
                table[dis] = table.get(dis,0)+1
            for v in table.itervalues():
                ret += v*(v-1)
        return ret
        