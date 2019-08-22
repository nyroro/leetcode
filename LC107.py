# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root ==None:
            return ret
        q = [(root, 0)]
        qi = 0
        
        while qi<len(q):
            t = q[qi]
            qi+=1
            if t[1]>=len(ret):
                ret.append([])
            ret[t[1]].append(t[0].val)
            if t[0].left !=None:
                q.append((t[0].left, t[1]+1))
            if t[0].right != None:
                q.append((t[0].right, t[1]+1))
            
        return ret[::-1]
            
            