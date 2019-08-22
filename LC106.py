# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        val = postorder[-1]
        root = TreeNode(postorder[-1])
        mid = -1
        for i in xrange(len(inorder)):
            if inorder[i] == val:
                mid = i
        l_inorder = inorder[:mid]
        r_inorder = inorder[mid+1:]
        l_postorder = postorder[:mid]
        r_postorder = postorder[mid:-1]
        root.left = self.buildTree(l_inorder, l_postorder)
        root.right = self.buildTree(r_inorder, r_postorder)
        return root
        
        
        