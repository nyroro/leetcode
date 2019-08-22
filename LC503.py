class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        stack = [(nums[0],0)]
        ret = [-1]*len(nums)
        for i in xrange(1, len(nums)):
            if len(stack)==0  or  nums[i]<=stack[-1][0]:
                stack.append((nums[i],i))
            else:
                while len(stack)>0 and nums[i]>stack[-1][0]:
                    ret[stack[-1][1]] = nums[i]
                    stack.pop(-1)
                stack.append((nums[i],i))
        print ret
        for i in xrange(0, len(nums)):
            while len(stack)>0:
                if nums[i]>stack[-1][0]:
                    ret[stack[-1][1]] = nums[i]
                    stack.pop(-1)
                elif stack[-1][1]<=i:
                    stack.pop(-1)
                else:
                    break
        return ret
        
                        
                    