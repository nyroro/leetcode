# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root ==None:
            return 0
        que = [(root, 0, 0)]
        table = {}
        
        qi = 0
        while qi<len(que):
            root, depth, index = que[qi]
            if depth not in table:
                table[depth] = [index, index]
            else:
                table[depth][0] = min(table[depth][0], index)
                table[depth][1] = max(table[depth][1], index)
            qi+=1
            if root.left!=None:
                que.append((root.left, depth+1, 2*index))
            if root.right!=None:
                que.append((root.right, depth+1, 2*index+1))
        ret = 0
        for v in table.itervalues():
            ret = max(ret, v[1]-v[0]+1)
        return ret
                
            
        