import copy
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret = []
        for i in xrange(len(nums)):
            if i> 0 and nums[i]==nums[i-1]:
                continue
            for j in xrange(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                sum_t = target - nums[i]-nums[j]
                tmp_ret = self.solve(nums, sum_t, j+1, len(nums)-1)
                for t in tmp_ret:
                    ret.append([nums[i],nums[j]]+list(t))
        return ret
                
                
    def solve(self, nums, target, l, r):
        ret = set()
        while l<r:
            if nums[l]+nums[r] == target:
                ret.add((nums[l],nums[r]))
                l+=1
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                r-=1
        return list(ret)
        