# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ret = [0]
        def dfs(root, pre):
            if root == None:
                return
            val = root.val
            if val == sum:
                ret[0] += 1
            for i in xrange(len(pre)-1, -1, -1):
                val += pre[i]
                if val == sum:
                    ret[0] += 1
            next_pre = pre+[root.val]
            dfs(root.left, next_pre)
            dfs(root.right, next_pre)
        dfs(root, [])
        return ret[0]