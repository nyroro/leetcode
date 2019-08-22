class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(list(set(nums)))
        table = {v:i for i,v in enumerate(sorted_nums)}
        bi_tree = [0]*(len(table)+1)
        ret = [0]*len(nums)
        
        def update(i):
            i=i+1
            while i<=len(table):
                bi_tree[i]+=1
                i += i&(-i)
                
        def query(i):
            res = 0
            i=i+1
            while i>0:
                res += bi_tree[i]
                i -= i&(-i)
            return res
        
        for i in xrange(len(nums)-1,-1,-1):
            ret[i] = query(table[nums[i]]-1)
            update(table[nums[i]])
        return ret