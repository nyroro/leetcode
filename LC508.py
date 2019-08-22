# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution(object):
    def findFrequentTreeSum(self, root):
        if root==None:
            return []
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if root == None:
                return 0,[]
            lval, lret = dfs(root.left)
            rval, rret = dfs(root.right)
            ret = [lval+rval+root.val]+lret+rret
            return ret[0], ret
        val,ret = dfs(root)
        
        c = Counter(ret)
        val = max(c.itervalues())
        return [key for key,value in c.iteritems() if value==val]