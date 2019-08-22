class Solution(object):
    def reverse(self, nums, a, b):
        for i in xrange((b-a)/2):
            nums[a+i], nums[b-i-1] =  nums[b-i-1], nums[a+i]
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-k)
        self.reverse(nums, len(nums)-k, len(nums))
        self.reverse(nums, 0, len(nums))