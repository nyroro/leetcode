import heapq
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k==1:
            return nums
        arr_l = []
        arr_r = []
        in_left = [False]*len(nums)
        num_l = 0
        num_r = 0
        ret = []
        for i in xrange(0,k):
            heapq.heappush(arr_l, (-nums[i], i))
            in_left[i] = True
            num_l+=1
            if len(arr_l)>k/2:
                val, index = arr_l[0]
                heapq.heappop(arr_l)
                in_left[index] = False
                num_l-=1
                heapq.heappush(arr_r, (-val, index))
                num_r+=1
        if k%2==1:
            ret.append(arr_r[0][0])
        else:
            ret.append(0.5*(arr_r[0][0]+(-arr_l[0][0])))
        # print arr_l, arr_r
            
        for i in xrange(k,len(nums)):
            
            # delete left num
            if in_left[i-k]:
                num_l-=1
            else:
                num_r-=1
            while len(arr_l)>0 and arr_l[0][1]<=i-k:
                heapq.heappop(arr_l)
            while len(arr_r)>0 and arr_r[0][1]<=i-k:
                heapq.heappop(arr_r)
            
            # add right num
            if len(arr_r)>0 and nums[i]<=arr_r[0][0]:
                heapq.heappush(arr_l, (-nums[i],i))
                in_left[i]=True
                num_l+=1
            else:
                heapq.heappush(arr_r, (nums[i], i))
                in_left[i] = False
                num_r+=1
            # adjust two heap
            while num_l<k/2:
                val, index = arr_r[0]
                if index>i-k:
                    heapq.heappush(arr_l, (-val, index))
                    num_l += 1
                    in_left[index] = True
                    num_r -= 1
                heapq.heappop(arr_r)
            while num_l>k/2:
                val, index = arr_l[0]
                if index>i-k:
                    heapq.heappush(arr_r, (-val, index))
                    in_left[index] = False
                    num_r += 1
                    num_l -= 1
                heapq.heappop(arr_l)
                
            
            while len(arr_l)>0 and arr_l[0][1]<=i-k:
                heapq.heappop(arr_l)
            while len(arr_r)>0 and arr_r[0][1]<=i-k:
                heapq.heappop(arr_r)
            if k%2 == 1:
                ret.append(arr_r[0][0])
            else:
                ret.append(0.5*(arr_r[0][0]+(-arr_l[0][0])))
        return ret
            
        