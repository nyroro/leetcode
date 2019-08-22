# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        table = {}
        if root==None:
            return []
        def findNum(root, val):
            if root == None:
                return 0
            ret = findNum(root.left, val)+findNum(root.right, val)
            if val == root.val:
                ret+=1
            return ret
        def findAns(root):
            if root == None:
                return (None, -1)
            findAns(root.left)
            findAns(root.right)
            num = findNum(root, root.val)
            table.setdefault(num,[]).append(root.val)
        findAns(root)
        print table
        val = max(table.keys())
        return table[val]