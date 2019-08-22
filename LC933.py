# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        left, right = self.handle(root)
        return left
        
    def handle(self, root):
        if root.left !=None:
            left, rightest = self.handle(root.left)
            rightest.right = root
            root.left = None
        else:
            left = root
        if root.right == None:
            return left, root
        rleft,rightest = self.handle(root.right)
        root.right = rleft
        return left, rightest
        