# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.ret = []
        if root is None:
            return []
        self.dfs(root, sum-root.val, [root.val])
        return self.ret
    
    def dfs(self, root, sum, l):
        if sum == 0:
            if root.left is None and root.right is None:
                self.ret.append(copy.copy(l))
                return
        if root.left:
            l.append(root.left.val)
            self.dfs(root.left, sum-root.left.val,l)
            l.pop(-1)
        if root.right:
            l.append(root.right.val)
            self.dfs(root.right, sum-root.right.val,l)
            l.pop(-1)
        