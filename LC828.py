class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)%2==0 or reduce(lambda x,y:x^y, nums) == 0
        