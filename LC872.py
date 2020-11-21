# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        ret = []
        def leafs(root):
            if root == None:
                return
            if root.left == None and root.right == None:
                ret.append(root.val)
                return
            leafs(root.left)
            leafs(root.right)
        leafs(root1)
        ret1 = ret
        ret = []
        leafs(root2)
        ret2 = ret
        return len(ret1) == len(ret2) and all([t[0] == t[1] for t in zip(ret1, ret2)])