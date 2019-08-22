# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ret, num1 = self.find(root.left, k)
        if ret is not None:
            return ret
        if k-num1 == 1:
            return root.val
        ret, num2 = self.find(root.right, k-num1-1)
        return ret
        
    def find(self, root, k):
        if root == None:
            return None, 0
        ret, num1 = self.find(root.left, k)
        if ret is not None:
            return ret,num1
        
        if k-num1 == 1:
            return root.val, 0
        ret, num2 = self.find(root.right, k-num1-1)
        if ret is not None:
            return ret, num2
        return ret, num1+1+num2