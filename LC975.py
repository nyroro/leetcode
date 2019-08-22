# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        ret = 0
        if root == None:
            return ret
        
        if L<=root.val<=R:
            ret += root.val
        if root.val<=R:
            ret += self.rangeSumBST(root.right, L, R)
        if root.val>=L:
            ret += self.rangeSumBST(root.left, L, R)
        return ret
        
        
        