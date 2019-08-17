import bisect
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sums = [0]
        for t in nums:
            sums.append(sums[-1]+t)
        l=0
        r=0
        ret = 10**18
        for r in xrange(len(nums)):
            if nums[l]!=nums[r]:
                t1 = nums[l]*l-sums[l]
                t2 = sums[len(nums)]-sums[r] - nums[r-1]*(len(nums)-r)
                # print l,t1,r,t2
                l=r
                ret = min(t1+t2,ret)
        t1 = nums[l]*l-sums[l]
        ret = min(t1,ret)
        return ret
                
                
            
        