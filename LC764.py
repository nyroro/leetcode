"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret = []
        que = [(root, 0)]
        qi = 0
        while qi<len(que):
            t = que[qi]
            qi+=1
            if len(ret)<=t[1]:
                ret.append([t[0].val])
            else:
                ret[t[1]].append(t[0].val)
            for child in t[0].children:
                que.append((child, t[1]+1))
        
        return ret
        