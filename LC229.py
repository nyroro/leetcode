class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maj1, cnt1 = None,0
        maj2, cnt2 = None,0
        
        for t in nums:
            if cnt1 == 0 and t!= maj2:
                maj1 = t
                cnt1 = 0
            elif cnt2 == 0 and t != maj1:
                maj2 = t
                cnt2 = 0
            if t == maj1:
                cnt1 += 1
            elif t== maj2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        ret = []
        if nums.count(maj1) > len(nums)//3:
            ret.append(maj1)
        if nums.count(maj2) > len(nums)//3 and maj2 != maj1:
            ret.append(maj2)
        return ret
        