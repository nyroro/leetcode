from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        m = max(c.values())
        return [t for t,v in c.iteritems() if v == m][0]
        