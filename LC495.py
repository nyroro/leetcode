class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ret = 0
        now = 0
        for t in timeSeries:
            if t>=now:
                now = t+duration
                ret+=duration
            else:
                ret+=duration-(now-t)
                now = t+duration
        return ret
        