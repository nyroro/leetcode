# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def dfs(root, depth):
            if root == None:
                return
            
            if len(ret)<depth:
                ret.append(root.val)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        dfs(root,1)
        return ret
        