class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        if s%k!=0:
            return False
        self.arr = [s/k]*k
        nums.sort(reverse=True)
        def dfs(i):
            if i==len(nums):
                return sum(self.arr) == 0
            for j in xrange(k):
                self.arr[j]-=nums[i]
                if self.arr[j]>=0:
                    if dfs(i+1):
                        return True
                
                self.arr[j]+=nums[i]
                if self.arr[j] == s/k:
                    break
            return False
        return dfs(0)
        