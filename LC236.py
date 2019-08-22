# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Node(object):
    def __init__(self, node, pre, level):
        self.val = node.val
        self.pre = pre
        self.level = level
        self.left = None
        self.right = None
        self.node = node
        
def reconstruct(root, p, q, pre, level):
    if root == None:
        return None, None, None
    troot = Node(root, pre, level)
    left, p1, q1 = reconstruct(root.left, p, q, troot, level+1)
    right, p2, q2 = reconstruct(root.right, p, q, troot, level+1)
    root = troot
    root.left = left
    root.right = right
    p_ret = None
    if p1:
        p_ret = p1
    elif p2:
        p_ret = p2
    elif root.node == p:
        p_ret = root
    q_ret = None 
    if q1:
        q_ret = q1
    elif q2:
        q_ret = q2
    elif root.node == q:
        q_ret = root
    return root, p_ret, q_ret
    

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root, p, q = reconstruct(root, p, q, None, 0)
        
        while p.level > q.level:
            p = p.pre
        while q.level > p.level:
            q = q.pre
        while p!=q:
            p = p.pre
            q = q.pre
        return p.node
        