class Solution(object):
            
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        class Node(object):
            def __init__(self):
                self.left = None
                self.right = None
        if len(nums)<=1:
            return 0
        root = Node()
        def insert(num):
            now = root
            for i in xrange(31,-1,-1):
                if num&(1<<i) == 0:
                    if now.left == None:
                        now.left = Node()
                    now = now.left
                else:
                    if now.right == None:
                        now.right = Node()
                    now = now.right
            
        def query(num):
            now = root
            ret = 0
            for i in xrange(31,-1,-1):
                if num&(1<<i)==0:
                    if now.right != None:
                        now=now.right
                        ret = ret*2+1
                    else:
                        now = now.left
                        ret = ret*2
                else:
                    if now.left != None:
                        now = now.left
                        ret = ret*2+1
                    else:
                        now = now.right
                        ret = ret*2
            return ret
            
                
                
        insert(nums[0])
        ret = 0
        for i in xrange(1, len(nums)):
            ret = max(ret, query(nums[i]))
            insert(nums[i])
        return ret
        
        