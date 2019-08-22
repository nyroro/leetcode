import copy
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums = sorted(nums)
        ret = []
        def dfs(now, index):
            if len(now)>=2:
                ret.append(copy.copy(now))
            s = set()
            for i in xrange(index, len(nums)):
                if len(now)==0 or now[-1]<=nums[i]:
                    if nums[i] not in s:
                        s.add(nums[i])
                        now.append(nums[i])
                        dfs(now, i+1)
                        now.pop(-1)
            
        dfs([], 0)
        return ret
        