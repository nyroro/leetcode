class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = [0]
        if len(nums)==0:
            return 0
        def merge(nums, l, r):
            if l==r:
                return
            mid = (l+r)/2
            merge(nums, l,mid)
            merge(nums, mid+1,r)
            li = l
            ri = mid+1
            # print nums[l:mid+1], nums[mid+1:r+1]
            while li<=mid and ri<=r:
                if nums[li]>nums[ri]*2:
                    # print nums[li], nums[ri]
                    ret[0]+=mid-li+1
                    ri+=1
                else:
                    li+=1
            li = l
            ri = mid+1
            tmp = []
            while li<=mid and ri<=r:
                if nums[li]<nums[ri]:
                    tmp.append(nums[li])
                    li+=1
                else:
                    tmp.append(nums[ri])
                    ri+=1
            while li<=mid:
                tmp.append(nums[li])
                li+=1
            while ri<=r:
                tmp.append(nums[ri])
                ri+=1
            nums[l:r+1] = tmp
            
        merge(nums, 0, len(nums)-1)
        return ret[0]