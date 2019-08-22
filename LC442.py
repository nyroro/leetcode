from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = Counter(nums)
        return [key for key,value in c.iteritems() if value>=2]