# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pre = None
        self.ret = 0xffffffff
        self.dfs(root)
        return self.ret
        
    def dfs(self,root):
        if root.left:
            self.dfs(root.left)
        if self.pre!=None:
            self.ret = min(self.ret, abs(root.val-self.pre))
        self.pre = root.val
        if root.right:
            self.dfs(root.right)
        