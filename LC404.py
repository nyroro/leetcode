# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root == None:
                return False, 0
            isLeave = root.left == None and root.right == None
            tleft, lval = dfs(root.left)
            tRight, rval = dfs(root.right)
            ret  = lval+rval
            if tleft:
                ret+=root.left.val
            return isLeave, ret
            
        isLeave, val = dfs(root)
        return val
        