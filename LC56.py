class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        ret = []
        for t in intervals:
            if len(ret) == 0:
                ret.append(t)
            else:
                if t[0] > ret[-1][1]:
                    ret.append(t)
                elif t[1] > ret[-1][1]:
                    ret[-1][1] = t[1]
        return ret
        