# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        q = []
        ret = [[]]
        q.append((root, 0))
        now = 0
        while len(q)>0:
            flag = q[0][1]
            if now == flag:
                pass
            else:
                now = flag
                ret.append([])
            
            root, flag = q.pop(0)
            ret[-1].append(root.val)
            
            
            if root.left:
                q.append((root.left, 1-flag))
            if root.right:
                q.append((root.right, 1-flag))
                
        for i in xrange(1,len(ret),2):
            ret[i] = ret[i][::-1]
        return ret
                
        