class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ret = 0
        for i in xrange(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i+2
            for j in xrange(i+1, len(nums)-1):
                t = nums[i]+nums[j]
                l = k
                r = len(nums)-1
                while l<=r:
                    mid = (l+r)/2
                    if nums[mid] >= t:
                        r = mid - 1
                    else:
                        l = mid
                    if l+1 >= r:
                        if nums[r] < t:
                            k = r
                        elif nums[l] < t:
                            k = l
                        else:
                            k = j
                        break
                ret += k-j
        return ret
                            
                
        