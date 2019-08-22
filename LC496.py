import bisect
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in xrange(len(nums1)):
            t = nums1[i]
            index = nums2.index(t)
            for j in xrange(index+1, len(nums2)):
                if nums2[j]>t:
                    ret.append(nums2[j])
                    break
            else:
                ret.append(-1)
        return ret
            
        