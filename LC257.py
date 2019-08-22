# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        def path(root, tmp_str):
            if root == None:
                return
            if tmp_str != "":
                tmp_str+="->"+str(root.val)
            else:
                tmp_str=str(root.val)
            if root.left == None and root.right==None:
                ret.append(tmp_str)
                return
            path(root.left, tmp_str)
            path(root.right,tmp_str)
        path(root, "")
        return ret
            
        