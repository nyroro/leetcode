# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        l = []
        def dfs(root):
            if root == None:
                return
            l.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        l.sort()
        return min([l[i+1] - l[i] for i in range(len(l)-1)])