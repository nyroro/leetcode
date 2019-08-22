"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root, depth):
            if root is None:
                return 0
            ret = depth
            
            if root.children is None:
                return ret
            for child in root.children:
                ret = max(dfs(child,depth+1), ret)
            return ret
        return dfs(root,1)
        