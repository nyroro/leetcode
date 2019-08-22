# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        arr = []
        for i,t in enumerate(intervals):
            arr.append((t[0], i))
        arr = sorted(arr)
        ret = []
        for t in intervals:
            k = bisect.bisect(arr, (t[1],-1))
            if k>=len(arr):
                ret.append(-1)
            else:
                ret.append(arr[k][1])
        return ret
            
        