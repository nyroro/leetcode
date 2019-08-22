class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        n = len(nums1)+len(nums2)
        m = n//2 + 1
        
        l1=0
        l2=0
        t = [None, None]
        def put(num):
            t[1] = t[0]
            t[0] = num
        
        while l1+l2<m and l1 <len(nums1) and l2<len(nums2):
            if nums1[l1] < nums2[l2]:
                put(nums1[l1])
                l1+=1
            else:
                put(nums2[l2])
                l2+=1
        while l1+l2<m and l1<len(nums1):
            put(nums1[l1])
            l1+=1
        while l1+l2<m and l2<len(nums2):
            put(nums2[l2])
            l2+=1
        print t
        if n%2==1:
            return t[0]
        else:
            return 1.0*(t[0]+t[1])/2
            
                
        