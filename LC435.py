class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals)
        now = intervals[0][1]
        ret = 0
        for i in xrange(1, len(intervals)):
            if intervals[i][0]<now:
                if intervals[i][1]<now:
                    now = intervals[i][1]
                ret+=1
            else:
                now = intervals[i][1]
        return ret